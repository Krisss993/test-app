from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import json
from dotenv import load_dotenv

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from langchain_chat.models import Conversation, ChatMessage
from django.http import JsonResponse, HttpResponseBadRequest
from django.http import FileResponse
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_history_aware_retriever
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain.chains import create_retrieval_chain
import os
from django.conf import settings
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough

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



runnable_with_history = RunnableWithMessageHistory(
    llm,
    get_session_history,
)



output_parser = StrOutputParser()
# Chain
chain = prompt | llm.with_config({"run_name": "model"}) | output_parser.with_config({"run_name": "Assistant"})

class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()

        # Send a message confirming connection
        await self.send(text_data=json.dumps({
            "message": "WebSocket connected."
        }))

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Parse the incoming message
        text_data_json = json.loads(text_data)
        
        if 'conversation_id' in text_data_json:
            print('CONVERSATION ID IS:', text_data_json['conversation_id'])
            self.conversation_id = text_data_json['conversation_id']
        else:
            message = text_data_json['message']
            print(message)
            
            # Retrieve chat history from memory or initialize it
            chat_history = get_session_history(self.conversation_id)
            conversation = await self.get_conversation(self.conversation_id)

            # Save the user's message to the database
            await self.save_message(conversation, self.scope["user"].username, message, is_user=True, is_ai=False)
            print('MESSAGE SAVED')

            # Prepare input for the chatbot
            session_config = {
                'configurable': {
                    'session_id': str(self.conversation_id),
                }
            }

            # Send the user's message back to the WebSocket
            await self.send(text_data=json.dumps({
                'message': message,
                'sender': self.scope["user"].username
            }))
            print('MESSAGE SENT')

            ai_message = ""
            try:
                # Stream the response from the chatbot
                async for chunk in runnable_with_history.astream_events(
                        {'message': [HumanMessage(content=message)]},
                        config=session_config,
                        version="v2"):

                    kind = chunk["event"]
                    if kind == "on_chat_model_start":
                        await self.send(text_data=json.dumps({
                            'run_id': 2,
                            'sender': 'Assistant',
                            'event': 'on_chat_model_start',
                        }))
                    elif kind == "on_chat_model_stream":
                        ai_message += chunk['data']['chunk'].content
                        await self.send(text_data=json.dumps({
                            'message': chunk['data']['chunk'].content,
                            'sender': 'Assistant',
                            'event': 'on_chat_model_stream',
                            'run_id': 2
                        }))

                # Save the full AI message to the database
                if ai_message:
                    await self.save_message(conversation, "Assistant", ai_message, is_user=False, is_ai=True)
                    await self.send(text_data=json.dumps({
                        'message': ai_message,
                        'sender': "Assistant"
                    }))
                    print('MESSAGE SENT TO WEBSOCKET', json.dumps({
                        'message': ai_message,
                        'sender': "Assistant"
                    }))

            except Exception as e:
                print('Response not working', e)
                print(f"Failed with input message: {message}")
                print(f"Failed with input message: {ai_message}")

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Send the message to WebSocket
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

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request, conversation_id=None):

    # Get all conversations created by the user
    conversations = Conversation.objects.filter(user=request.user).order_by('-created_at')
    # If a conversation ID is provided, get the conversation, otherwise create a new one
    conversation = None
    messages = []
    if conversation_id:
        # Get the specific conversation and its messages
        conversation = get_object_or_404(Conversation, id=conversation_id, user=request.user)
        messages = ChatMessage.objects.filter(conversation_id=conversation_id).order_by('timestamp')
    else:
        # Create a new conversation if no conversation ID is provided
        conversation = Conversation.objects.create(user=request.user)
        return redirect('langchain_chat:chat', conversation_id=conversation.id)
    # Pass the conversation to the template if necessary
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
    conversation.delete()  # Delete the conversation
    return redirect('langchain_chat:conversation_list')  # Redirect to a new chat after deletion
