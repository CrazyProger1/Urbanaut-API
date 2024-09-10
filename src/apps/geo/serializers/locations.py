from rest_framework import serializers
from drf_extra_fields import geo_fields as geo

from src.apps.geo.models import Location


class LocationRetrieveSerializer(serializers.ModelSerializer):
    point = geo.PointField(read_only=True)

    class Meta:
        model = Location
        fields = "__all__"


class LocationCreateSerializer(serializers.ModelSerializer):
    point = geo.PointField()

    class Meta:
        model = Location
        fields = ("point",)
