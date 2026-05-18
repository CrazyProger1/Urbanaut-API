from django_filters import rest_framework as filters

from src.apps.accounts.services.db import filter_where_member


class TeamFilter(filters.FilterSet):
    is_member = filters.BooleanFilter(method="filter_where_member")

    def filter_where_member(self, queryset, name, value):
        return filter_where_member(source=queryset, user=self.request.user, is_member=value)
