from rest_framework import serializers

from src.apps.abandoned.models import Area
from src.utils.django.geo import PolygonField


class AreaListSerializer(serializers.ModelSerializer):
    polygon = PolygonField()

    class Meta:
        model = Area
        fields = (
            "id",
            "name",
            "polygon",
        )


class AreaRetrieveSerializer(serializers.ModelSerializer):
    security = serializers.SlugRelatedField(
        slug_field="level",
        read_only=True,
    )
    polygon = PolygonField()

    class Meta:
        model = Area
        fields = "__all__"
