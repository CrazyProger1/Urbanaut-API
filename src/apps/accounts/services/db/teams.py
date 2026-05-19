from django.conf import settings
from django.db import models
from django.db.models import Q
from modeltranslation.utils import build_localized_fieldname

from src.apps.accounts.models import Team, TeamMember
from src.utils.django.db import Source, get_queryset


def get_all_teams():
    return Team.objects.all()


def get_all_team_members():
    return TeamMember.objects.all()


def count_user_teams(user) -> int:
    return TeamMember.objects.filter(member=user).count()


def add_creator_as_member(team: Team) -> TeamMember:
    return TeamMember.objects.create(team=team, member=team.created_by)


def filter_where_member(source: Source[Team], user, is_member: bool) -> models.QuerySet[Team]:
    queryset = get_queryset(source=source)

    if is_member:
        return queryset.filter(members=user)
    else:
        return queryset.filter(~Q(members=user))


def search_teams(
        term: str = None, source: Source[Team] = Team
) -> models.QuerySet[Team]:
    queryset = get_queryset(source=source)
    query = Q()
    term = term.lower()

    if term:
        for lang_code, _ in settings.LANGUAGES:
            field = build_localized_fieldname("name", lang_code)
            query |= Q(**{f"{field}__icontains": term})

    return queryset.filter(query).distinct()
