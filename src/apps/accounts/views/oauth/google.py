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
    GoogleOauthRedirectURIRequestSerializer,
)
from src.apps.accounts.services.db import (
    get_or_create_user_by_email,
    get_referral_code_or_none,
)
from src.apps.accounts.services.oauth import (
    generate_google_oauth_redirect_uri,
    authenticate_google_oauth_code,
    decode_id_token,
    save_google_oauth_cache,
    load_google_oauth_cache,
)
from src.apps.accounts.services.referrals import try_apply_referral_code
from src.apps.accounts.services.users import publish_user_created

logger = logging.getLogger(__name__)


class GoogleOauthRedirectURIView(APIView):
    @extend_schema(
        request=GoogleOauthRedirectURIRequestSerializer,
        responses=GoogleOauthRedirectURIResponseSerializer,
    )
    def post(self, request, **kwargs):
        token = secrets.token_urlsafe(16)

        serializer = GoogleOauthCallbackRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        logger.debug("Generating Google Oauth redirect URI: %s", token)

        save_google_oauth_cache(token=token, cache=serializer.validated_data)

        return Response(
            {"redirect_uri": generate_google_oauth_redirect_uri(state=token)}
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
        oauth_code = request_serializer.validated_data["code"]
        token = request_serializer.validated_data["state"]

        extras = load_google_oauth_cache(token=token)
        referral_code = extras.pop("code", None)

        try:
            tokens = authenticate_google_oauth_code(code=oauth_code)
        except HTTPError:
            logger.error("Failed to authenticate the provided code or state: %s", oauth_code)
            raise AuthenticationFailed(
                detail="Failed to authenticate the provided code or state.",
            )

        google_user = decode_id_token(tokens["id_token"])

        internal_user, created = get_or_create_user_by_email(email=google_user["email"])

        if created and referral_code:
            referral_code_obj = get_referral_code_or_none(code=referral_code)

            if referral_code_obj:
                try_apply_referral_code(code=referral_code_obj, user=internal_user)

        response_serializer = GoogleOauthCallbackResponseSerializer(
            instance={
                "user": internal_user,
            },
        )
        publish_user_created(user=internal_user)
        logger.info("User authenticated via Google Oauth: %s", google_user)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
