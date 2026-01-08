from django_filters import rest_framework as filters


class BoundsFilter(filters.Filter):
    def filter(self, queryset, value):
        pass
