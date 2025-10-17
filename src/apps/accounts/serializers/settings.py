from rest_framework import serializers

from src.apps.accounts.models import Settings


class SettingsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = (
            "language",
            "is_notifications_enabled",
            "theme",
        )


class SettingsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = (
            "language",
            "is_notifications_enabled",
            "theme",
        )
