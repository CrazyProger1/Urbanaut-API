from src.config.settings.base import (
    TITLE,
    DESCRIPTION,
    VERSION,
)

SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,
    "PERSIST_AUTH": True,
    "DEFAULT_MODEL_RENDERING": "example",
    "DISPLAY_OPERATION_ID": True,
    "DOC_EXPANSION": "none",
    "SUPPORTED_SUBMIT_METHODS": ["get", "post", "put", "delete", "patch"],
    "HEADERS": {"Accept-Language": "ru"},
}
SPECTACULAR_SETTINGS = {
    "TITLE": TITLE,
    "DESCRIPTION": DESCRIPTION,
    "VERSION": VERSION,
    "SERVE_INCLUDE_SCHEMA": True,
    "SCHEMA_PATH_PREFIX": r"/api/v[0-9]",
    "COMPONENT_SPLIT_REQUEST": True,
    "SECURITY": [{"TMAAuth": []}],
    "AUTHENTICATION_WHITELIST": [],
    "COMPONENT_SECURITY_SCHEMES": {
        "TMAAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Telegram-Mini-Apps authentication using an encoded header. Provide data as key-value pairs.",
        }
    },
}
