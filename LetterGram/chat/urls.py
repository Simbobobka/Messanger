from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [    
    path('profile/', views.profile, name='profile'),       
    path('', views.chatPage, name="home"),       
    path('<int:chat_id>/', views.chatPage, name='chat-detail'),
    path('start-chat/<int:user_id>/', views.startChat, name='start-chat'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)