from rest_framework import serializers

from src.apps.abandoned.models import AbandonedObject
from src.apps.abandoned.serializers.areas import AbandonedAreaRetrieveSerializer
from src.apps.accounts.serializers import UserRetrieveSerializer
from src.apps.geo.serializers import (
    LocationRetrieveSerializer,
    LocationCreateSerializer,
)
from src.apps.permissions.serializers import PermissionSerializerMixin


class AbandonedObjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedObject
        fields = (
            "area",
            "name",
            "description",
            "security_level",
            "preservation_level",
            "difficulty_level",
            "created_at",
            "updated_at",
            "built_at",
            "abandoned_at",
            "creator",
            "location",
        )


class AbandonedObjectRetrieveSerializer(serializers.ModelSerializer, PermissionSerializerMixin):
    area = AbandonedAreaRetrieveSerializer(read_only=True)
    creator = UserRetrieveSerializer(read_only=True)
    location = LocationRetrieveSerializer(read_only=True)

    class Meta:
        model = AbandonedObject
        fields = (
            "area",
            "name",
            "description",
            "security_level",
            "preservation_level",
            "difficulty_level",
            "created_at",
            "updated_at",
            "built_at",
            "abandoned_at",
            "creator",
            "location",
        )


class AbandonedObjectCreateSerializer(serializers.ModelSerializer):
    location = LocationCreateSerializer()

    class Meta:
        model = AbandonedObject
        fields = (
            "id",
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
