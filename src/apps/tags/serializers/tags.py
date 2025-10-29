from rest_framework import serializers

from src.apps.tags.models import Tag


class TagRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
