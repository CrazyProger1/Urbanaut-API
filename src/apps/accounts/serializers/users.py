from rest_framework import serializers

from src.apps.accounts.models import User
from src.apps.accounts.serializers.settings import SettingsRetrieveSerializer


class CurrentUserSerializer(serializers.ModelSerializer):
    settings = SettingsRetrieveSerializer(read_only=True)
    usernames = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "settings",
            "usernames",
        )
