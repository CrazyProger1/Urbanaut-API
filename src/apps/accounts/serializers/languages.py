from rest_framework import serializers


class LanguageListSerializer(serializers.Serializer):
    name = serializers.CharField()
    code = serializers.CharField()

    def to_representation(self, obj):
        return {"code": obj[0], "name": obj[1]}
