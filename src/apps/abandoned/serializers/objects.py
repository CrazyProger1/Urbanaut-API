from rest_framework import serializers

from src.apps.abandoned.models import AbandonedObject
from src.apps.abandoned.serializers import (
    AbandonedObjectCategoryRetrieveSerializer,
    AbandonedAreaRetrieveSerializer,
)
from src.apps.accounts.serializers import UserRetrieveSerializer
from src.apps.geo.serializers import (
    LocationRetrieveSerializer,
    LocationCreateSerializer,
)
from src.apps.media.serializers import FileRetrieveSerializer
from src.apps.permissions.serializers import PermissionSerializerMixin


class AbandonedObjectListSerializer(serializers.ModelSerializer):
    photo = serializers.CharField(read_only=True)

    class Meta:
        model = AbandonedObject
        fields = (
            "id",
            "area",
            "name",
            "description",
            "short_description",
            "security_level",
            "preservation_level",
            "difficulty_level",
            "created_at",
            "updated_at",
            "built_at",
            "abandoned_at",
            "created_by",
            "location",
            "photo",
        )


class AbandonedObjectRetrieveSerializer(serializers.ModelSerializer, PermissionSerializerMixin):
    area = AbandonedAreaRetrieveSerializer(read_only=True)
    created_by = UserRetrieveSerializer(read_only=True)
    location = LocationRetrieveSerializer(read_only=True)
    photos = FileRetrieveSerializer(many=True, read_only=True)
    categories = AbandonedObjectCategoryRetrieveSerializer(read_only=True, many=True)

    class Meta:
        model = AbandonedObject
        fields = (
            "id",
            "area",
            "name",
            "description",
            "short_description",
            "security_level",
            "preservation_level",
            "difficulty_level",
            "created_at",
            "updated_at",
            "built_at",
            "abandoned_at",
            "created_by",
            "location",
            "photos",
            "categories",
        )


class AbandonedObjectCreateSerializer(serializers.ModelSerializer):
    location = LocationCreateSerializer()

    class Meta:
        model = AbandonedObject
        fields = (
            "area",
            "name",
            "description",
            "security_level",
            "preservation_level",
            "difficulty_level",
            "built_at",
            "abandoned_at",
            "location",
        )
