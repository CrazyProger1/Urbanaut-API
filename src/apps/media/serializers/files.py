from rest_framework import serializers

from src.apps.media.models import File


class FileListSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField()

    class Meta:
        model = File
        exclude = ("file", "created_at", "updated_at", "creator")


class FileRetrieveSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField()

    class Meta:
        model = File
        exclude = ("file", "creator")


class FileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("file", "is_hidden")

    def validate_file(self, value):
        return value
