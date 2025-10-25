from drf_spectacular.utils import extend_schema_field
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
    achievements = serializers.SerializerMethodField()
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

    @extend_schema_field(AchievementRetrieveSerializer(many=True))
    def get_achievements(self, instance):
        achievements = instance.achievements.all().order_by("-weight")
        return AchievementRetrieveSerializer(achievements, many=True).data

    def to_representation(self, instance):
        data = super().to_representation(instance=instance)
        # TODO: remove mock
        data["metrics"] = [
            {
                "name": "Karma",
                "value": 3000,
            },
            {
                "name": "Experience",
                "value": 100000,
            },
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
