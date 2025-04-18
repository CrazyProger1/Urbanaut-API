from rest_framework import serializers

from src.apps.accounts.serializers import UserRetrieveSerializer
from src.apps.blog.models import BlogPost
from src.apps.blog.serializers.topics import BlogTopicRetrieveSerializer
from src.apps.permissions.serializers import PermissionSerializerMixin


class BlogPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = (
            "id",
            "title",
            "topic",
            "created_by",
            "created_at",
            "updated_at",
            "published_at",
        )


class BlogPostRetrieveSerializer(serializers.ModelSerializer, PermissionSerializerMixin):
    created_by = UserRetrieveSerializer(read_only=True)
    topic = BlogTopicRetrieveSerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = (
            "id",
            "title",
            "topic",
            "created_by",
            "created_at",
            "updated_at",
            "published_at",
            "content",
            "has_delete_permission",
            "has_change_permission",
        )


class BlogPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        exclude = (
            "id",
            "created_by",
            "created_at",
            "updated_at",
        )
