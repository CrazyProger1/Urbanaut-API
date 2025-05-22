from rest_framework import serializers

from src.apps.accounts.serializers import UserRetrieveSerializer, UserListSerializer
from src.apps.blog.models import BlogPost
from src.apps.blog.serializers.topics import (
    BlogTopicRetrieveSerializer,
    BlogTopicListSerializer,
)
from src.apps.media.serializers import FileRetrieveSerializer
from src.apps.permissions.serializers import PermissionSerializerMixin


class BlogPostListSerializer(serializers.ModelSerializer):
    topics = BlogTopicListSerializer(read_only=True, many=True)
    created_by = UserListSerializer(read_only=True)
    photo = serializers.CharField(read_only=True)

    class Meta:
        model = BlogPost
        fields = (
            "id",
            "title",
            "topics",
            "summary",
            "created_by",
            "created_at",
            "updated_at",
            "published_at",
            "photo",
        )


class BlogPostRetrieveSerializer(
    serializers.ModelSerializer, PermissionSerializerMixin
):
    created_by = UserRetrieveSerializer(read_only=True)
    topics = BlogTopicRetrieveSerializer(read_only=True, many=True)
    files = FileRetrieveSerializer(read_only=True, many=True)
    photo = serializers.CharField(read_only=True)

    class Meta:
        model = BlogPost
        fields = (
            "id",
            "title",
            "topics",
            "created_by",
            "created_at",
            "updated_at",
            "published_at",
            "content",
            "has_delete_permission",
            "has_change_permission",
            "files",
            "photo",
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
