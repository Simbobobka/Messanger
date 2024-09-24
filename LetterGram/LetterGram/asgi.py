
import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter , URLRouter
from chat import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LetterGram.settings')
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
    "http": django_asgi_app,
    "websocket" : AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )    
        )
    }
)

ASGI_APPLICATION = 'LetterGram.asgi.application'
