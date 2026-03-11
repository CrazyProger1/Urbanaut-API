from rest_framework import serializers

from src.apps.abandoned.enums import PreservationLevel, SecurityLevel
from src.apps.geo.services.db import get_active_countries
from src.apps.tags.services.db import get_all_tags


class MapRequestSerializer(serializers.Serializer):
    tags = serializers.MultipleChoiceField(
        choices=get_all_tags().values_list("tag", flat=True),
        required=False,
    )
    query = serializers.CharField(
        required=False,
    )
    ai_query = serializers.CharField(
        required=False,
    )
    preservation = serializers.ChoiceField(
        required=False,
        choices=PreservationLevel,
    )
    security = serializers.ChoiceField(
        required=False,
        choices=SecurityLevel,
    )
    has_security = serializers.BooleanField(
        required=False,
        help_text="Show secured only"
    )
    country = serializers.ChoiceField(
        required=False,
        choices=get_active_countries().values_list(
            "tld",
            flat=True,
        ),
    )
    is_favorite = serializers.BooleanField(
        required=False,
        help_text="Show favorite only"
    )
    is_private = serializers.BooleanField(
        required=False,
        help_text="Show private only"
    )
    is_supposed = serializers.BooleanField(
        required=False,
        help_text="Show supposed only"
    )


class FeatureGeometrySerializer(serializers.Serializer):
    type = serializers.ChoiceField(
        choices=("Polygon", "Point"),
        default="Point",
    )
    coordinates = serializers.SerializerMethodField()

    def get_coordinates(self, instance):
        return instance


class FeaturePropertySerializer(serializers.Serializer):
    def to_representation(self, instance):
        return instance


class FeatureSerializer(serializers.Serializer):
    type = serializers.CharField(default="Feature")
    geometry = FeatureGeometrySerializer()
    properties = FeaturePropertySerializer(many=True)


class MapResponseSerializer(serializers.Serializer):
    type = serializers.CharField(default="FeatureCollection")
    features = FeatureSerializer(many=True)
