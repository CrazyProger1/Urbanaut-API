from rest_framework import serializers

from src.apps.abandoned.enums import PreservationLevel, SecurityLevel
from src.apps.geo.services.db import get_active_countries
from src.apps.tags.services.db import get_all_tags


class MapRequestSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tags"].choices = list(get_all_tags().values_list("tag", flat=True))
        self.fields["country"].choices = list(
            get_active_countries().values_list("tld", flat=True)
        )

    tags = serializers.MultipleChoiceField(
        required=False,
        choices=[],
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
        help_text="Show secured only",
        allow_null=True,
    )
    country = serializers.ChoiceField(
        required=False,
        choices=[],
    )
    is_favorite = serializers.BooleanField(
        required=False,
        help_text="Show favorite only",
        allow_null=True,
    )
    is_private = serializers.BooleanField(
        required=False,
        help_text="Show private only",
        allow_null=True,
    )
    is_supposed = serializers.BooleanField(
        required=False,
        help_text="Show supposed only",
        allow_null=True,
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
