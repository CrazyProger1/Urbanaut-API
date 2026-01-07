from rest_framework import serializers

from src.apps.accounts.models import Settings
from src.apps.geo.serializers import CountryRetrieveSerializer


class SettingsRetrieveSerializer(serializers.ModelSerializer):
    country = CountryRetrieveSerializer(read_only=True)

    class Meta:
        model = Settings
        fields = (
            "language",
            "is_notifications_enabled",
            "theme",
            "country",
        )

    def to_representation(self, instance: Settings):
        data = super().to_representation(instance=instance)
        if not instance.is_country_visible:
            data["country"] = None
        return data


class SettingsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = (
            "language",
            "is_notifications_enabled",
            "theme",
        )
