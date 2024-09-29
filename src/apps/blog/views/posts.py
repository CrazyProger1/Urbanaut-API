from rest_framework import viewsets, generics, permissions

from src.apps.blog.serializers import BlogPostListSerializer, BlogPostRetrieveSerializer
from src.apps.blog.services.db import get_unhidden_blog_posts, get_user_blog_posts


class BlogPostViewSet(
    viewsets.GenericViewSet,
    generics.ListAPIView,
    generics.RetrieveAPIView,
):
    queryset = get_unhidden_blog_posts()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = BlogPostListSerializer
    serializer_classes = {
        "list": BlogPostListSerializer,
        "retrieve": BlogPostRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset | get_user_blog_posts(user=self.request.user)
        return self.queryset
