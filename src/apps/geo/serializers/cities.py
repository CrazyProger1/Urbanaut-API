from rest_framework import serializers

from src.apps.geo.models import City


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("name",)
