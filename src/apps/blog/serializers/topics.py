from rest_framework import serializers

from src.apps.blog.models import BlogTopic


class BlogTopicRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTopic
        fields = (
            "id",
            "name",
            "description",
            "created_at",
            "is_closed",
        )
