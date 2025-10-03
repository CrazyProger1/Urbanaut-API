from typing import TypedDict
from urllib.parse import urljoin, quote, urlencode

import jwt
import requests

from src.utils.django.settings import default_settings


class UserTokens(TypedDict):
    access_token: str
    id_token: str


class UserData(TypedDict):
    email: str
    email_verified: bool
    name: str
    picture: str
    family_name: str
    given_name: str


def generate_google_oauth_redirect_uri(state: str):
    params = {
        "client_id": default_settings.GOOGLE_OAUTH_CLIENT_ID,
        "redirect_uri": urljoin(default_settings.BASE_URL, str(default_settings.GOOGLE_OAUTH_CALLBACK_URL)),
        "response_type": "code",
        "scope": " ".join(default_settings.GOOGLE_OAUTH_SCOPES),
        "access_type": default_settings.GOOGLE_OAUTH_ACCESS_TYPE,
        "state": state,
    }

    query_string = urlencode(params, quote_via=quote)
    return f"{default_settings.GOOGLE_OAUTH_REDIRECT_BASE_URL}?{query_string}"


def authenticate_google_oauth_code(code: str) -> UserTokens:
    response = requests.post(
        url=default_settings.GOOGLE_OAUTH_TOKEN_URL,
        data={
            "client_id": default_settings.GOOGLE_OAUTH_CLIENT_ID,
            "client_secret": default_settings.GOOGLE_OAUTH_CLIENT_SECRET,
            "grant_type": "authorization_code",
            "redirect_uri": urljoin(default_settings.BASE_URL, str(default_settings.GOOGLE_OAUTH_CALLBACK_URL)),
            "code": code,
        },
    )
    response.raise_for_status()
    data = response.json()
    return UserTokens(**data)


def decode_id_token(id_token: str) -> UserData:
    data = jwt.decode(
        id_token,
        algorithms=["RS256"],
        options={"verify_signature": False},
    )

    return UserData(**data)
