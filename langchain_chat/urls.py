from django.urls import path  
from . import views  
from .views import conversation_list, index


app_name = 'langchain_chat'
  

urlpatterns = [  
    path('conversations/', conversation_list, name='conversation_list'),
    path('chat/<int:conversation_id>/', index, name='chat'),
    path('chat/', views.index, name='chat'),
    path('chat/<int:conversation_id>/delete/', views.delete_conversation, name='delete_conversation'),
    path('chat/new/', views.create_new_chat, name='create_new_chat'),

]
