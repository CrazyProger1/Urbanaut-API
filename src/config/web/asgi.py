import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.config.settings")

django_asgi_app = get_asgi_application()

from src.apps.accounts.middlewares import WebsocketQueryAuthMiddleware
from src.apps.accounts.urls import websocket_urlpatterns

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            WebsocketQueryAuthMiddleware(URLRouter(websocket_urlpatterns))
        ),
    }
)
