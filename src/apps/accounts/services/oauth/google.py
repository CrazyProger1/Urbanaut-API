from urllib.parse import urljoin, quote, urlencode

from src.utils.django.settings import default_settings


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
