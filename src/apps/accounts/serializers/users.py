from rest_framework import serializers

from src.apps.accounts.models import User
from src.apps.accounts.serializers.achievements import AchievementRetrieveSerializer
from src.apps.accounts.serializers.metrics import MetricRetrieveSerializer
from src.apps.accounts.serializers.settings import SettingsRetrieveSerializer


class CurrentUserSerializer(serializers.ModelSerializer):
    settings = SettingsRetrieveSerializer(read_only=True)
    usernames = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="username",
    )
    achievements = AchievementRetrieveSerializer(many=True, read_only=True)
    metrics = MetricRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "settings",
            "usernames",
            "first_name",
            "last_name",
            "achievements",
            "metrics",
            "bio",
            "created_at",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance=instance)
        # TODO: remove mock
        data["metrics"] = [
            {
                "name": "Reports",
                "value": 50,
            },
            {
                "name": "Friends",
                "value": 30,
            },
            {
                "name": "Teams",
                "value": 1,
            },
            {
                "name": "Followers",
                "value": 500,
            },
            {
                "name": "Places",
                "value": 300,
            },
        ]
        return data
