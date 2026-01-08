from rest_framework import serializers


class MetricRetrieveSerializer(serializers.Serializer):
    name = serializers.CharField()
    value = serializers.IntegerField()
