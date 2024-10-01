from django.urls import path , include
from chat.consumers import ChatConsumer
from django.urls import re_path

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<chat_id>\d+)/$', ChatConsumer.as_asgi()),
    
] 