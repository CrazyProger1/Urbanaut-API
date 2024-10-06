from rest_framework import serializers

from src.apps.abandoned.models import AbandonedArea

from src.apps.permissions.serializers import PermissionSerializerMixin


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
        )


class AbandonedAreaRetrieveSerializer(serializers.ModelSerializer, PermissionSerializerMixin):
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
        )
