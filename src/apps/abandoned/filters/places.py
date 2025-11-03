from django_filters import rest_framework as filters

from src.apps.abandoned.models import Place
from src.apps.tags.services.db.tags import get_all_tags


class PlaceFilter(filters.FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        field_name="tags__tag",
        to_field_name="tag",
        queryset=get_all_tags(),
    )
    class Meta:
        model = Place
        fields = (
            "name",
            "area",
        )
