import json
from dotenv import load_dotenv

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_chat.models import Conversation, ChatMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


load_dotenv('.env')


chatbotmemory={}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in chatbotmemory:
        chatbotmemory[session_id] = ChatMessageHistory()
    return chatbotmemory[session_id]    

llm = ChatGroq(model="llama-3.1-70b-versatile")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
       MessagesPlaceholder(variable_name='message')

])

chain = prompt | llm

runnable_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
)


class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.run_id=0
        await self.accept()

        await self.send(text_data=json.dumps({
            "message": "WebSocket connected."
        }))


    async def disconnect(self, close_code):
        pass


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        if 'conversation_id' in text_data_json:
            print('CONVERSATION ID IS:', text_data_json['conversation_id'])
            self.conversation_id = text_data_json['conversation_id']
        else:
            message = text_data_json['message']
            conversation = await self.get_conversation(self.conversation_id)
            await self.save_message(conversation, self.scope["user"].username, message, is_user=True, is_ai=False)
            print('MESSAGE SAVED')

            session_config = {
                'configurable': {
                    'session_id': str(self.conversation_id),
                }
            }

            await self.send(text_data=json.dumps({
                'message': message,
                'sender': self.scope["user"].username
            }))
            print('MESSAGE SENT')

            ai_message = ""
            try:
                print('RESPONSE LOOP STARTED')
                print(f'SELF RUN ID: {self.run_id}')
                self.run_id += 1

                async for chunk in runnable_with_history.astream_events(
                        {
                            'message': [HumanMessage(content=message)],
                         },
                        config=session_config,
                        version="v2"):

                    kind = chunk["event"]

                    if kind == "on_chat_model_start":
                        await self.send(text_data=json.dumps({
                            'run_id': self.run_id,
                            'sender': 'Assistant',
                            'event': 'on_chat_model_start',
                        }))

                    elif kind == "on_chat_model_stream":
                        ai_message += chunk['data']['chunk'].content
                        await self.send(text_data=json.dumps({
                            'message': chunk['data']['chunk'].content,
                            'sender': 'Assistant',
                            'event': 'on_chat_model_stream',
                            'run_id': self.run_id,
                        }))

                if ai_message:
                    await self.save_message(conversation, "Assistant", ai_message, is_user=False, is_ai=True)
                    await self.send(text_data=json.dumps({
                        'message': ai_message,
                        'sender': "Assistant"
                    }))
                    print(f'MESSAGE SENT TO WEBSOCKET: {ai_message}')

            except Exception as e:
                print(f"Response not working: {e}")
                print(f"Failed with user input message: {message}")
                print(f"Failed with AI input message: {ai_message}")


    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))


    @sync_to_async
    def get_conversation(self, conversation_id):
        return Conversation.objects.get(pk=conversation_id)


    @sync_to_async
    def save_message(self, conversation, sender, message, is_user, is_ai):
        return ChatMessage.objects.create(
            conversation=conversation, 
            sender=sender, 
            message=message, 
            is_user_message=is_user,
            is_ai_message=is_ai
        )


@login_required
def index(request, conversation_id=None):
    conversations = Conversation.objects.filter(user=request.user).order_by('-created_at')
    if conversation_id:
        conversation = get_object_or_404(Conversation, id=conversation_id, user=request.user)
    else:
        if conversations.exists():
            conversation = conversations.first()
        else:
            conversation = Conversation.objects.create(user=request.user)
            return redirect('langchain_chat:chat', conversation_id=conversation.id)

    messages = ChatMessage.objects.filter(conversation_id=conversation.id).order_by('timestamp')

    chat_history = ChatMessageHistory()
    for message in messages:
        if message.is_user_message:
            chat_history.add_user_message(HumanMessage(content=message.message))
        elif message.is_ai_message:
            chat_history.add_ai_message(AIMessage(content=message.message))

    chatbotmemory[str(conversation.id)] = chat_history

    return render(request, 'langchain_chat/chat.html', {
        'conversation': conversation,
        'messages': messages,
        'conversations': conversations,
    })

@login_required
def conversation_list(request):
    conversations = Conversation.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'langchain_chat/conversation_list.html', {'conversations': conversations})


@login_required
def delete_conversation(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id, user=request.user)
    conversation.delete()
    return redirect('langchain_chat:conversation_list')

@login_required
def create_new_chat(request):
    new_conversation = Conversation.objects.create(user=request.user)
    return redirect('langchain_chat:chat', conversation_id=new_conversation.id)
