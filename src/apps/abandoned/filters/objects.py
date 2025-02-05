import django_filters as filters
from django.conf import settings
from django.db.models import Q
from modeltranslation.utils import build_localized_fieldname
from rest_framework_gis.filterset import GeoFilterSet

from src.apps.abandoned.models import AbandonedObject
from src.apps.abandoned.services.db import search_abandoned_objects
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
    query = filters.CharFilter(method="search", label="Search")

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
            "query",
        )

    def search(self, queryset, name, value):
        if value in ([], (), {}, "", None):
            return queryset

        return search_abandoned_objects(
            queryset=queryset,
            term=value,
            fields=(
                "name",
                "description",
                "short_description",
            ),
        )
