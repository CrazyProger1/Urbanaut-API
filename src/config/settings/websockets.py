from datetime import timedelta

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

WEBSOCKET_TOKEN_TTL = timedelta(hours=1)

WEBSOCKET_USER_GROUP = "user_{id}"
WEBSOCKET_SYSTEM_GROUP = "system"
WEBSOCKET_COMMON_GROUPS = (
    WEBSOCKET_SYSTEM_GROUP,
)
WEBSOCKET_NOTIFICATION_EVENT = "notification"
