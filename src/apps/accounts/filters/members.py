from django_filters import rest_framework as filters
from rest_framework import exceptions

from src.apps.accounts.models import TeamMember
from src.apps.accounts.services.db.teams import get_team_or_none


class TeamMemberFilter(filters.FilterSet):
    team = filters.CharFilter(method="filter_by_team")

    class Meta:
        model = TeamMember
        fields = ("team",)

    def filter_by_team(self, queryset, name, value):
        team = get_team_or_none(pk=value)

        if not team:
            raise exceptions.NotFound(detail="Team not found")

        return queryset.filter(team=team)
