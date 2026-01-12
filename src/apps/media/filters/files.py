import django_filters as filters

from src.apps.media.models import File


class FileFilter(filters.FilterSet):
    ordering = filters.OrderingFilter(
        fields=(
            ("id", "id"),
            ("created_at", "created_at"),
            ("updated_at", "updated_at"),
        ),
    )

    class Meta:
        model = File
        fields = (
            "created_by",
            "type",
        )