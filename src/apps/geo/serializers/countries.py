from rest_framework import serializers

from src.apps.geo.models import Country


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("tld", "name")
