from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q

from src.apps.permissions.models import ObjectPermission, ModelPermission
from src.apps.permissions.utils import get_permissions_field, get_owner_field, is_owner
from src.utils.db import filter_objects

User = get_user_model()


def get_model_permissions(model: type[models.Model]) -> ModelPermission | None:
    return filter_objects(model, Q(model=model)).first()


def get_object_permissions(obj: models.Model) -> ObjectPermission:
    return getattr(
        obj,
        get_permissions_field(type(obj)),
    )


def get_user_group(obj: models.Model, user: User = None):
    if user.is_superuser:
        return 0
    elif user.is_staff:
        return 100
    elif is_owner(obj, user):
        return 200
    elif user.is_authentificated:
        return 300
    return 400


def has_create_permission(user: User, model: type[models.Model]) -> bool:
    return False


def has_view_permission(user: User, obj: models.Model) -> bool:
    object_permissions = get_object_permissions(obj=obj)
    try:
        primary_permissions = object_permissions.user_permissions.get(user=user)
        return primary_permissions.has_view_permission
    except models.ObjectDoesNotExist:
        group = get_user_group(obj, user)
        return object_permissions.visibility_level >= group


def has_change_permission(user: User, obj: models.Model) -> bool:
    object_permissions = get_object_permissions(obj=obj)
    try:
        primary_permissions = object_permissions.user_permissions.get(user=user)
        return primary_permissions.has_change_permission
    except models.ObjectDoesNotExist:
        group = get_user_group(obj, user)
        return object_permissions.changebility_level >= group


def has_delete_permission(user: User, obj: models.Model) -> bool:
    object_permissions = get_object_permissions(obj=obj)
    try:
        primary_permissions = object_permissions.user_permissions.get(user=user)
        return primary_permissions.has_delete_permission
    except models.ObjectDoesNotExist:
        group = get_user_group(obj, user)
        return object_permissions.deletebility_level >= group
