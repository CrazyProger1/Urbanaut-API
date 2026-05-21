from rest_framework import serializers


class MetricRetrieveSerializer(serializers.Serializer):
    key = serializers.CharField()
    value = serializers.IntegerField()
