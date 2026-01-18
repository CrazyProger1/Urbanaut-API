import logging
from datetime import timedelta

import jwt
from django.conf import settings
from django.utils import timezone

from src.apps.accounts.exceptions import InvalidWebsocketTokenError
from src.apps.accounts.services.db import get_user_or_none

logger = logging.getLogger(__name__)


def generate_websocket_token(
    user, ttl: timedelta = settings.WEBSOCKET_TOKEN_TTL
) -> str:
    now = timezone.now()
    payload = {
        "id": str(user.id),
        "exp": now + ttl,
        "iat": now,
    }
    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm="HS256",
    )
    logger.info("Generated websocket token for user #%s with ttl %s", user.id, ttl)
    return token


def verify_websocket_token(token: str):
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user = get_user_or_none(id=data["id"])
        if not user:
            raise InvalidWebsocketTokenError(
                message=f"User specified in payload not found: {data}", token=token
            )

        logger.info("Websocket token of user #%s verified successfully", user.id)
        return user
    except jwt.InvalidTokenError:
        logger.warning("Invalid websocket token: %s", token)
        raise InvalidWebsocketTokenError(
            message=f"Failed to decode websocket token: {token}", token=token
        )
