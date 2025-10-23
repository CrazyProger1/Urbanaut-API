from rest_framework import serializers

from src.apps.accounts.models import Achievement


class AchievementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = (
            "id",
            "name",
            "weight",
        )