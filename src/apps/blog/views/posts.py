from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response

from src.apps.blog.serializers import (
    BlogPostListSerializer,
    BlogPostRetrieveSerializer,
    BlogPostCreateSerializer,
)
from src.apps.blog.services.db import get_available_blog_posts
from src.apps.permissions.permissions import HasPermission


class BlogPostViewSet(
    viewsets.GenericViewSet,
    generics.ListAPIView,
    generics.RetrieveAPIView,
    generics.CreateAPIView,
):
    queryset = get_available_blog_posts()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, HasPermission)
    serializer_class = BlogPostListSerializer
    serializer_classes = {
        "list": BlogPostListSerializer,
        "retrieve": BlogPostRetrieveSerializer,
        "create": BlogPostCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return get_available_blog_posts(user=self.request.user)
        return self.queryset

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)

    @extend_schema(
        request=BlogPostCreateSerializer,
        responses={
            201: BlogPostRetrieveSerializer,
        },
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        response_serializer = BlogPostRetrieveSerializer(instance)
        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )
