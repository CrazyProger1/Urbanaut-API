import secrets

from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.accounts.services.oauth import generate_google_oauth_redirect_uri


class GoogleOauthRedirectURIView(APIView):
    def get(self, request, **kwargs):
        return Response({"redirect_uri": generate_google_oauth_redirect_uri(state=secrets.token_urlsafe(16))})


class GoogleOauthCallbackView(APIView):
    def post(self, request, **kwargs):
        pass
