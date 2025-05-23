import django_filters as filters

from src.apps.blog.models import BlogPost
from src.apps.blog.services.db import search_blog_posts


class BlogPostFilter(filters.FilterSet):
    query = filters.CharFilter(method="search", label="Search")

    ordering = filters.OrderingFilter(
        fields=(
            ("id", "id"),
            ("created_at", "created_at"),
            ("updated_at", "updated_at"),
            ("published_at", "published_at"),
        ),
    )

    class Meta:
        model = BlogPost
        fields = (
            "created_by",
            "query",
        )

    def search(self, queryset, name, value):
        if value in ([], (), {}, "", None):
            return queryset

        return search_blog_posts(
            source=queryset,
            term=value,
            fields=(
                "title",
                "summary",
                "content",
            ),
        )
