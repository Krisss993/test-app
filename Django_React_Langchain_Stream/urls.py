from django.contrib import admin
from django.urls import path, include
import core.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/',include('langchain_stream.urls')),
    path('convs/',include('langchain_chat.urls')),
    path('accounts/', include('allauth.urls')),
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('ml/', include('ml.urls', namespace='ml')),
]
