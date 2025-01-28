import django_filters as filters
from django.conf import settings
from django.db.models import Q
from modeltranslation.utils import build_localized_fieldname
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
    query = filters.CharFilter(field_name="search", label="Search")

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
            "search",
        )

    def search(self, queryset, name, value):
        if value in ([], (), {}, "", None):
            return queryset

        query = Q()

        for field_name in ("name", "description"):
            for lang_code, _ in settings.LANGUAGES:
                lookup = f"{build_localized_fieldname(field_name, lang_code)}__icontains"
                query |= Q(**{lookup: value})
        return queryset.filter(query)
