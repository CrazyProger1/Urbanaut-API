from rest_framework import serializers

from src.apps.abandoned.models import AbandonedArea


class AbandonedAreaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedArea
        fields = (
            "id",
            "created_at",
            "updated_at",
            "area",
            "name",
            "description",
            "creator",
            "security_level",
            "is_hidden",
        )


class AbandonedAreaRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedArea
        fields = (
            "id",
            "created_at",
            "updated_at",
            "area",
            "name",
            "description",
            "creator",
            "security_level",
            "is_hidden",
        )
