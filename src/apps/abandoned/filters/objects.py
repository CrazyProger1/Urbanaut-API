import django_filters as filters

from src.apps.abandoned.models import AbandonedObject


class AbandonedObjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains", field_name="name")
    description = filters.CharFilter(lookup_expr="icontains", field_name="description")

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
