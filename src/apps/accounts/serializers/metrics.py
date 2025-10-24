from rest_framework import serializers


class MetricsRetrieveSerializer(serializers.Serializer):
    reports = serializers.IntegerField(default=0)
    friends = serializers.IntegerField(default=0)
    teams = serializers.IntegerField(default=0)
    followers = serializers.IntegerField(default=0)
    places = serializers.IntegerField(default=0)
