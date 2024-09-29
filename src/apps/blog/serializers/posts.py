from modeltranslation.utils import get_translation_fields
from rest_framework import serializers

from src.apps.accounts.serializers import UserRetrieveSerializer
from src.apps.blog.models import BlogPost
from src.apps.blog.serializers.topics import BlogTopicRetrieveSerializer


class BlogPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        exclude = (
            "is_hidden",
            "content",
            *get_translation_fields("content"),
        )


class BlogPostRetrieveSerializer(serializers.ModelSerializer):
    creator = UserRetrieveSerializer(read_only=True)
    topic = BlogTopicRetrieveSerializer(read_only=True)

    class Meta:
        model = BlogPost
        exclude = (
            "is_hidden",
        )
