from rest_framework import serializers


class GlobalStatsRetrieveSerializer(serializers.Serializer):
    places_count = serializers.IntegerField(read_only=True)
    areas_count = serializers.IntegerField(read_only=True)
    users_count = serializers.IntegerField(read_only=True)
    countries_count = serializers.IntegerField(read_only=True)
    expeditions_count = serializers.IntegerField(read_only=True)
