from rest_framework import serializers

from src.apps.accounts.serializers import UserRetrieveSerializer, UserListSerializer
from src.apps.media.models import File
from src.apps.media.utils.files import get_filetype


class FileListSerializer(serializers.ModelSerializer):
    src = serializers.ReadOnlyField()

    class Meta:
        model = File
        exclude = ("file",)


class FileRetrieveSerializer(serializers.ModelSerializer):
    src = serializers.ReadOnlyField()
    created_by = UserListSerializer(read_only=True)

    class Meta:
        model = File
        exclude = ("file",)


class FileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("file", "is_hidden")

    def validate_file(self, value):
        return value

    def create(self, validated_data):
        validated_data["type"] = get_filetype(file=validated_data["file"])
        return super().create(validated_data=validated_data)
