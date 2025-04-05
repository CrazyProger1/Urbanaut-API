from rest_framework import serializers

from src.apps.accounts.models import Settings


class SettingsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = (
            "id",
            "language",
        )
