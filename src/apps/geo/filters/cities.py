from django.contrib.postgres.search import TrigramSimilarity
from django_filters import rest_framework as filters

from src.apps.geo.models import City


class CityFilter(filters.FilterSet):
    query = filters.CharFilter(method="search")

    class Meta:
        model = City
        fields = ("query",)

    def search(self, queryset, name, value):
        return (
            queryset.annotate(
                similarity=TrigramSimilarity("name", value),
            )
            .filter(similarity__gt=0.3)
            .order_by("-similarity")
        )
