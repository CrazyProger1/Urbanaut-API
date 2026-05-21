from django.db import models
from django.db.models import Q

from src.apps.accounts.models import ObjectPermissionsMixin, User, Team, ObjectPermission
from src.apps.accounts.services.db import get_user_teams
from src.utils.django.db import Source, get_queryset


def get_visible_permissions(user: User) -> models.QuerySet[ObjectPermission]:
    teams = get_user_teams(user=user)
    return ObjectPermission.objects.filter(
        Q(user_object_permissions__user=user, user_object_permissions__is_visible=True) |
        Q(team_object_permissions__team__in=teams, team_object_permissions__is_visible=True)
    ).distinct()


def get_editable_permissions(user: User) -> models.QuerySet[ObjectPermission]:
    teams = get_user_teams(user=user)
    return ObjectPermission.objects.filter(
        Q(user_object_permissions__user=user, user_object_permissions__is_editable=True) |
        Q(team_object_permissions__team__in=teams, team_object_permissions__is_editable=True)
    ).distinct()


def filter_visible_objects_for_user[T: ObjectPermissionsMixin](source: Source[T], user: User) -> models.QuerySet[T]:
    queryset = get_queryset(source=source)
    visible_perms = get_visible_permissions(user=user)
    return queryset.filter(permission__in=visible_perms)


def filter_editable_objects_for_user[T: ObjectPermissionsMixin](source: Source[T], user: User) -> models.QuerySet[T]:
    queryset = get_queryset(source=source)
    editable_perms = get_editable_permissions(user=user)
    return queryset.filter(permission__in=editable_perms)
