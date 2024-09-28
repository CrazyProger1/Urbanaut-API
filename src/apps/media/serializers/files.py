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
