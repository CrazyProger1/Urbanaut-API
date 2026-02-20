from rest_framework import serializers

from src.apps.abandoned.models import PlacePreservation, PlaceSecurity


class PlaceSecurityCreateRetrieveSerializer(serializers.ModelSerializer):
    """
    Doubts about the legality
    """
    class Meta:
        model = PlaceSecurity
        fields = (
            # "has_dogs",
            # "has_weapons",
            # "has_cameras",
            # "has_sensors",
            "has_security",
            # "level",
        )
        # read_only_fields = (
        #     "level",
        # )
