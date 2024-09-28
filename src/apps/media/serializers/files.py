from rest_framework import serializers

from src.apps.media.models import File
from src.apps.media.services.url import get_file_url


class FileListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = File
        exclude = ("file",)

    def get_url(self, obj: File):
        return get_file_url(file=obj)
