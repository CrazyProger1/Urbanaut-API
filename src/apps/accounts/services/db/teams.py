from django.db import models
from django.db.models import Q

from src.apps.accounts.models import Team, TeamMember
from src.utils.django.db import Source, get_queryset


def get_all_teams():
    return Team.objects.all()


def get_all_team_members():
    return TeamMember.objects.all()


def count_user_teams(user) -> int:
    return TeamMember.objects.filter(member=user).count()


def filter_where_member(source: Source[Team], user, is_member: bool) -> models.QuerySet[Team]:
    queryset = get_queryset(source=source)

    if is_member:
        return queryset.filter(members=user)
    else:
        return queryset.filter(~Q(members=user))
