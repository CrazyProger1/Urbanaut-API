from django_filters import rest_framework as filters

from src.apps.abandoned.models import Place


class PlaceFilter(filters.FilterSet):
    tags = filters.CharFilter(field_name="tags", lookup_expr="icontains")

    class Meta:
        model = Place
        fields = (
            "name",
            "area",
        )
