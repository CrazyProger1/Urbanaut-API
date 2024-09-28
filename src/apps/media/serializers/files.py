from rest_framework import serializers

from src.apps.accounts.serializers import UserRetrieveSerializer
from src.apps.media.models import File


class FileListSerializer(serializers.ModelSerializer):
    src = serializers.ReadOnlyField()

    class Meta:
        model = File
        exclude = (
            "file",
        )


class FileRetrieveSerializer(serializers.ModelSerializer):
    src = serializers.ReadOnlyField()
    creator = UserRetrieveSerializer(read_only=True)

    class Meta:
        model = File
        exclude = (
            "file",
        )


class FileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("file", "is_hidden")

    def validate_file(self, value):
        return value
