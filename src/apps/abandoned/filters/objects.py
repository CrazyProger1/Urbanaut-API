import django_filters as filters
from rest_framework_gis.filterset import GeoFilterSet

from src.apps.abandoned.models import AbandonedObject
from src.utils.filters import LocalizedFilter


class AbandonedObjectFilter(GeoFilterSet):
    name = LocalizedFilter(
        field_name="name",
        lookup_expr="icontains",
    )
    description = LocalizedFilter(
        field_name="description",
        lookup_expr="icontains",
    )

    ordering = filters.OrderingFilter(
        fields=(
            ("id", "id"),
            ("created_at", "created_at"),
            ("updated_at", "updated_at"),
            ("built_at", "built_at"),
            ("abandoned_at", "abandoned_at"),
        ),
    )

    class Meta:
        model = AbandonedObject
        fields = (
            "difficulty_level",
            "preservation_level",
            "security_level",
        )
