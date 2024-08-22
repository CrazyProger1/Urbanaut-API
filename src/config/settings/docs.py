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
    "TITLE": "Urbanaut-API",
    "DESCRIPTION": "Urbanaut API",
    "VERSION": "0.0.1",
    "SERVE_INCLUDE_SCHEMA": False,
}
