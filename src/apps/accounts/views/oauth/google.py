import logging
import secrets

from drf_spectacular.utils import extend_schema
from requests import HTTPError
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.accounts.serializers.oauth import (
    GoogleOauthCallbackRequestSerializer,
    GoogleOauthCallbackResponseSerializer,
    GoogleOauthRedirectURIResponseSerializer,
)
from src.apps.accounts.services.oauth import (
    generate_google_oauth_redirect_uri,
    authenticate_google_oauth_code,
    decode_id_token,
)

logger = logging.getLogger(__name__)


class GoogleOauthRedirectURIView(APIView):
    @extend_schema(
        responses=GoogleOauthRedirectURIResponseSerializer,
    )
    def get(self, request, **kwargs):
        state = secrets.token_urlsafe(16)
        logger.debug("Generating Google Oauth redirect URI: %s", state)
        return Response(
            {"redirect_uri": generate_google_oauth_redirect_uri(state=state)}
        )


class GoogleOauthCallbackView(APIView):

    @extend_schema(
        request=GoogleOauthCallbackRequestSerializer,
        responses=GoogleOauthCallbackResponseSerializer,
    )
    def post(self, request, **kwargs):
        logger.debug("Trying to authenticate client using Google OAuth...")
        request_serializer = GoogleOauthCallbackRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        code = request_serializer.validated_data["code"]
        try:
            tokens = authenticate_google_oauth_code(code=code)
        except HTTPError:
            logger.error("Failed to authenticate the provided code or state: %s", code)
            raise AuthenticationFailed(
                detail="Failed to authenticate the provided code or state.",
            )
        google_user = decode_id_token(tokens["id_token"])
        response_serializer = GoogleOauthCallbackResponseSerializer(
            instance=google_user,
        )
        logger.info("User authenticated via Google Oauth: %s", google_user)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
