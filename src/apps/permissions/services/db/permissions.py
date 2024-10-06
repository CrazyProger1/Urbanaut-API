import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q

from src.apps.permissions.models import ObjectPermission, ModelPermission
from src.apps.permissions.utils import get_permissions_field, get_user_group
from src.utils.db import filter_objects, create_object

User = get_user_model()

logger = logging.getLogger(__name__)


def create_object_permissions(**kwargs):
    return create_object(ObjectPermission, **kwargs)


def get_model_permissions(model: type[models.Model]) -> ModelPermission | None:
    return filter_objects(
        ModelPermission,
        Q(model=ContentType.objects.get_for_model(model)),
    ).first()


def get_object_permissions(obj: models.Model) -> ObjectPermission:
    return getattr(
        obj,
        get_permissions_field(type(obj)),
    )


def has_create_permission(user: User, model: type[models.Model]) -> bool:
    model_permissions = get_model_permissions(model)
    group = get_user_group(user=user)
    return model_permissions.createbility_level >= group


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
