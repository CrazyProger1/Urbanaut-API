from rest_framework import serializers

from src.apps.abandoned.models import Place
from src.apps.tags.serializers.tags import TagCreateSerializer
from src.utils.django.geo import PointField


class PlaceListSerializer(serializers.ModelSerializer):
    point = PointField()

    class Meta:
        model = Place
        fields = (
            "id",
            "name",
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
    tags = serializers.ListField(child=serializers.CharField(required=False), required=False)

    class Meta:
        model = Place
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_by",
            "created_at",
            "updated_at",
        )
