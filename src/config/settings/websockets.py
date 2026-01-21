from datetime import timedelta
from decouple import config

REDIS_HOST = config("REDIS_HOST", default="127.0.0.1")
REDIS_PORT = config("REDIS_PORT", cast=int, default=6379)

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(REDIS_HOST, REDIS_PORT)],
        },
    },
}

WEBSOCKET_TOKEN_TTL = timedelta(hours=1)

WEBSOCKET_USER_GROUP = "user_{id}"
WEBSOCKET_SYSTEM_GROUP = "system"
WEBSOCKET_COMMON_GROUPS = (WEBSOCKET_SYSTEM_GROUP,)
WEBSOCKET_NOTIFICATION_EVENT = "notification"
