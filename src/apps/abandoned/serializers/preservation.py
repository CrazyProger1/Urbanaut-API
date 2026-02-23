from rest_framework import serializers

from src.apps.abandoned.models import PlacePreservation


class PlacePreservationCreateRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacePreservation
        fields = (
            "has_floor",
            "has_roof",
            "has_walls",
            "has_windows",
            "has_doors",
            "has_internal_ceilings",
            "level",
        )
        read_only_fields = ("level",)
