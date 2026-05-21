from rest_framework import serializers

from src.apps.accounts.models import Achievement


class AchievementRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = (
            "id",
            "name",
            "weight",
            "icon",
            "significance",
            "slug",
            "description",
            "karma",
            "experience",
            "money",
        )


class AchievementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = (
            "id",
            "name",
            "slug",
        )
