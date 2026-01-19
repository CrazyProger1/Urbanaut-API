import logging

from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

from src.apps.accounts.exceptions import InvalidWebsocketTokenError
from src.apps.accounts.services.websockets import verify_websocket_token

User = get_user_model()
logger = logging.getLogger(__name__)


@database_sync_to_async
def try_verify_token(token: str) -> User | None:
    try:
        return verify_websocket_token(token=token)
    except InvalidWebsocketTokenError:
        return None


class WebsocketQueryAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        user = await try_verify_token(scope["query_string"].decode())
        if user:
            logger.info("User #%s authenticated successfully", user.id)

        scope["user"] = user or AnonymousUser()
        return await self.app(scope, receive, send)
