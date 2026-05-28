from rest_framework.exceptions import NotAuthenticated

from django_filters import rest_framework as filters

from src.apps.accounts.models import Team
from src.apps.accounts.services.db import filter_teams_where_member, search_teams


class TeamFilter(filters.FilterSet):
    is_member = filters.BooleanFilter(method="filter_where_member")
    query = filters.CharFilter(method="search")

    class Meta:
        model = Team
        fields = ("query",)

    def filter_where_member(self, queryset, name, value):
        user = self.request.user if self.request else None
        if not user or not user.is_authenticated:
            raise NotAuthenticated
        return filter_teams_where_member(
            source=queryset, user=user, is_member=value
        )

    def search(self, queryset, name, value):
        return search_teams(term=value, source=queryset)
