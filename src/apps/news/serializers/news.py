from rest_framework import serializers

from src.apps.news.models import News


class NewsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "subtitle",
            "published_at",
            "type",
            "has_more",
        )
