from rest_framework import serializers

from src.apps.accounts.models import Settings
from src.apps.geo.serializers import CountryRetrieveSerializer
from src.apps.geo.services.db import get_active_countries


class SettingsRetrieveSerializer(serializers.ModelSerializer):
    country = CountryRetrieveSerializer(read_only=True)

    class Meta:
        model = Settings
        fields = (
            "language",
            "is_notifications_enabled",
            "country",
        )


class CurrentSettingsRetrieveSerializer(serializers.ModelSerializer):
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
    country = serializers.SlugRelatedField(
        slug_field="tld",
        queryset=get_active_countries(),
    )

    class Meta:
        model = Settings
        fields = (
            "language",
            "is_notifications_enabled",
            "theme",
            "country",
        )
