from rest_framework import serializers

from src.apps.accounts.models import User
from src.apps.accounts.serializers.settings import SettingsSerializer


class CurrentUserSerializer(serializers.ModelSerializer):
    settings = SettingsSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "settings",
        )
