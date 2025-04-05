from rest_framework import serializers

from src.apps.accounts.models import Settings


class SettingsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = (
            "language",
            "is_animations_enabled",
            "is_notifications_enabled",
            "is_newsletters_enabled",
            "theme",
        )
