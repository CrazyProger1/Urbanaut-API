from typing import Any

from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, AuthUser

from src.apps.accounts.serializers import CurrentUserSerializer


class GoogleOauthCallbackRequestSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    state = serializers.CharField(required=True)


class GoogleOauthCallbackResponseSerializer(serializers.Serializer):
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    user = CurrentUserSerializer(read_only=True)

    token_class = RefreshToken

    def validate(self, attrs: dict[str, Any]) -> dict[str, str]:
        # TODO: refactor
        data = {}
        user = attrs["user"]
        refresh = self.get_token(user)
        data["user"] = CurrentUserSerializer(instance=user).data
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        update_last_login(user, user)
        return data

    @classmethod
    def get_token(cls, user: AuthUser) -> RefreshToken:
        return cls.token_class.for_user(user)


class GoogleOauthRedirectURIResponseSerializer(serializers.Serializer):
    redirect_uri = serializers.URLField()
