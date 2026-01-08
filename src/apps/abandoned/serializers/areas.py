from rest_framework import serializers

from src.apps.abandoned.models import Area
from src.apps.accounts.serializers import UserListSerializer
from src.apps.tags.services.db import get_all_tags
from src.utils.django.geo import PolygonField


class AreaCreateSerializer(serializers.ModelSerializer):
    polygon = PolygonField()
    tags = serializers.SlugRelatedField(
        slug_field="tag",
        many=True,
        queryset=get_all_tags(),
    )

    class Meta:
        model = Area
        fields = (
            "name",
            "description",
            "polygon",
            "parent",
            "tags",
            "is_private",
        )


class AreaListSerializer(serializers.ModelSerializer):
    polygon = PolygonField()

    class Meta:
        model = Area
        fields = (
            "id",
            "polygon",
        )


class AreaRetrieveSerializer(serializers.ModelSerializer):
    security = serializers.SlugRelatedField(
        slug_field="level",
        read_only=True,
    )
    polygon = PolygonField()
    tags = serializers.SlugRelatedField(
        slug_field="tag",
        many=True,
        read_only=True,
    )
    created_by = UserListSerializer(read_only=True)

    class Meta:
        model = Area
        fields = "__all__"
