from rest_framework import serializers

from src.apps.abandoned.models import AbandonedArea

from src.apps.permissions.serializers import PermissionSerializerMixin
from src.apps.ratings.serializers import RatingRetrieveSerializer


class AbandonedAreaListSerializer(serializers.ModelSerializer):
    rating = RatingRetrieveSerializer(read_only=True)

    class Meta:
        model = AbandonedArea
        fields = (
            "id",
            "created_at",
            "updated_at",
            "parent",
            "name",
            "description",
            "created_by",
            "security_level",
            "rating",
        )


class AbandonedAreaRetrieveSerializer(
    serializers.ModelSerializer, PermissionSerializerMixin
):
    rating = RatingRetrieveSerializer(read_only=True)

    class Meta:
        model = AbandonedArea
        fields = (
            "id",
            "created_at",
            "updated_at",
            "parent",
            "name",
            "description",
            "created_by",
            "security_level",
            "rating",
        )
