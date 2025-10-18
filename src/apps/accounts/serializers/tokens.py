from typing import Any

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from src.apps.accounts.serializers import CurrentUserSerializer


class TokenObtainPairWithUserSerializer(TokenObtainPairSerializer):
    user = CurrentUserSerializer(read_only=True)

    def validate(self, attrs: dict[str, Any]) -> dict[str, str]:
        data = super().validate(attrs=attrs)
        data["user"] = CurrentUserSerializer(instance=self.user).data
        return data
