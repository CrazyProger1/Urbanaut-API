from rest_framework import serializers

from src.apps.blog.models import BlogTopic


class BlogTopicRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTopic
        exclude = (
            "is_hidden",
        )
