from django.urls import path  
from . import views  
from .views import conversation_list, index


app_name = 'langchain_stream'
  

urlpatterns = [  
    path('conversations/', conversation_list, name='conversation_list'),
    path('chat/<int:conversation_id>/', index, name='chat'),
    path('chat/', views.index, name='chat'),
    path('chat/<int:conversation_id>/delete/', views.delete_conversation, name='delete_conversation'),
    path('upload/<int:conversation_id>/', views.upload_file, name='upload_file'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('file/<int:file_id>/delete/', views.delete_file, name='delete_file'),
    path('chat/new/', views.create_new_chat, name='create_new_chat'),
    
]
