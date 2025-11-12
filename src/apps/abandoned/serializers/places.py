from rest_framework import serializers

from src.apps.abandoned.models import Place
from src.apps.tags.services.db import get_all_tags
from src.utils.django.geo import PointField


class PlaceListSerializer(serializers.ModelSerializer):
    point = PointField()

    class Meta:
        model = Place
        fields = (
            "id",
            "point",
        )


class PlaceRetrieveSerializer(serializers.ModelSerializer):
    security = serializers.SlugRelatedField(
        slug_field="level",
        read_only=True,
    )
    preservation = serializers.SlugRelatedField(
        slug_field="level",
        read_only=True,
    )
    tags = serializers.SlugRelatedField(
        slug_field="tag",
        many=True,
        read_only=True,
    )
    point = PointField()

    class Meta:
        model = Place
        fields = "__all__"


class PlaceCreateSerializer(serializers.ModelSerializer):
    point = PointField()
    tags = serializers.SlugRelatedField(
        slug_field="tag",
        many=True,
        queryset=get_all_tags(),
    )

    class Meta:
        model = Place
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_by",
            "created_at",
            "updated_at",
            "is_private",
        )
