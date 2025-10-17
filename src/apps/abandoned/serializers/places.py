from rest_framework import serializers

from src.apps.abandoned.models import Place


class PlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            "id",
            "name",
        )


class PlaceRetrieveSerializer(serializers.ModelSerializer):
    security = serializers.SlugRelatedField(
        slug_field="level",
        read_only=True,
    )

    class Meta:
        model = Place
        fields = "__all__"


class PlaceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_by",
            "created_at",
            "updated_at",
        )
