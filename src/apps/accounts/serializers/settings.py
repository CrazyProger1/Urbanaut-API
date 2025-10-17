from rest_framework import serializers

from src.apps.accounts.models import Settings


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = (
            "language",
            "is_notifications_enabled",
            "theme",
        )

