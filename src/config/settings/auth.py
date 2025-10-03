from urllib.parse import urljoin

from decouple import config

from src.config.settings.base import BASE_FRONTEND_URL

GOOGLE_OAUTH_CLIENT_ID = config("GOOGLE_OAUTH_CLIENT_ID", cast=str)
GOOGLE_OAUTH_CLIENT_SECRET = config("GOOGLE_OAUTH_CLIENT_SECRET", cast=str)
GOOGLE_OAUTH_SCOPES = (
    "openid",
    "profile",
    "email",
)
GOOGLE_OAUTH_CALLBACK_URL = urljoin(BASE_FRONTEND_URL, "api/google/oauth/callback")
