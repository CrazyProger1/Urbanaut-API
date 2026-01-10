from django_filters import rest_framework as filters

from src.apps.abandoned.models import Place
from src.apps.abandoned.services.db import search_places
from src.apps.abandoned.services.ai import search_places_ai
from src.apps.tags.services.db.tags import get_all_tags
from src.utils.django.geo import BoundsSerializer


class PlaceFilter(filters.FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        field_name="tags__tag",
        to_field_name="tag",
        queryset=get_all_tags(),
    )
    query = filters.CharFilter(method="search")
    ai_query = filters.CharFilter(method="ai_search")
    preservation = filters.CharFilter(field_name="preservation__level")
    country = filters.CharFilter(field_name="address__country__tld")

    class Meta:
        model = Place
        fields = (
            "name",
            "area",
        )

    def search(self, queryset, name, value):
        return search_places(source=queryset, term=value)

    def ai_search(self, queryset, name, value):
        return search_places_ai(source=queryset, term=value)

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset=queryset)
        serializer = BoundsSerializer(data=self.data)

        if serializer.is_valid():
            bounds = serializer.bounds
            return queryset.filter(point__within=bounds)
        return queryset
