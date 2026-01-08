from rest_framework import serializers

from src.apps.abandoned.enums import PreservationLevel
from src.apps.abandoned.models import Place
from src.apps.abandoned.services.db import set_preservation_level
from src.apps.accounts.serializers import UserListSerializer
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
    created_by = UserListSerializer(
        read_only=True,
    )

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
    preservation = serializers.ChoiceField(
        choices=PreservationLevel,
        write_only=True,
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
            "preservation",
        )

    def create(self, validated_data):
        preservation = validated_data.pop("preservation", None)
        place = super().create(validated_data=validated_data)
        set_preservation_level(
            place=place,
            level=preservation,
        )
        return place
