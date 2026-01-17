import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from src.apps.notifications.urls import websocket_urlpatterns as notification_urls

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

django_asgi_app = get_asgi_application()

websocket_urlpatterns = [
    *notification_urls,
]

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
    }
)
