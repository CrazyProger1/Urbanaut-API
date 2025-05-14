from rest_framework import viewsets, generics, permissions

from src.apps.blog.serializers import (
    BlogTopicListSerializer,
    BlogTopicRetrieveSerializer,
)
from src.apps.blog.services.db import get_available_blog_topics
from src.apps.permissions.permissions import HasPermission


class BlogTopicViewSet(
    viewsets.GenericViewSet,
    generics.ListAPIView,
    generics.RetrieveAPIView,
):
    queryset = get_available_blog_topics()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, HasPermission)
    serializer_class = BlogTopicListSerializer
    serializer_classes = {
        "list": BlogTopicListSerializer,
        "retrieve": BlogTopicRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return get_available_blog_topics(user=self.request.user)
        return self.queryset
