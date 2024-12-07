import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q, QuerySet

from src.apps.permissions.models import ObjectPermission, ModelPermission
from src.apps.permissions.utils import get_permissions_field, get_user_group, get_owner_field
from src.utils.db import filter_objects, create_object

User = get_user_model()

logger = logging.getLogger(__name__)


def create_object_permissions(**kwargs):
    return create_object(ObjectPermission, **kwargs)


def get_model_permissions_or_none(model: type[models.Model]) -> ModelPermission | None:
    return filter_objects(
        ModelPermission,
        Q(model=ContentType.objects.get_for_model(model)),
    ).first()


def get_object_permissions_or_none(obj: models.Model) -> ObjectPermission:
    return getattr(
        obj,
        get_permissions_field(type(obj)),
    )


def has_create_permission(user: User, model: type[models.Model]) -> bool:
    model_permissions = get_model_permissions_or_none(model)

    if not model_permissions:
        return True

    try:
        primary_permissions = model_permissions.user_permissions.get(user=user)
        return primary_permissions.has_create_permission
    except models.ObjectDoesNotExist:
        group = get_user_group(user=user)
        return model_permissions.createbility_level >= group


def has_view_permission(user: User, obj: models.Model) -> bool:
    object_permissions = get_object_permissions_or_none(obj=obj)
    try:
        primary_permissions = object_permissions.user_permissions.get(user=user)
        return primary_permissions.has_view_permission
    except (models.ObjectDoesNotExist, TypeError):
        group = get_user_group(obj=obj, user=user)
        return object_permissions.visibility_level >= group


def has_change_permission(user: User, obj: models.Model) -> bool:
    object_permissions = get_object_permissions_or_none(obj=obj)
    try:
        primary_permissions = object_permissions.user_permissions.get(user=user)
        return primary_permissions.has_change_permission
    except (models.ObjectDoesNotExist, TypeError):
        group = get_user_group(obj=obj, user=user)
        return object_permissions.changebility_level >= group


def has_delete_permission(user: User, obj: models.Model) -> bool:
    object_permissions = get_object_permissions_or_none(obj=obj)
    try:
        primary_permissions = object_permissions.user_permissions.get(user=user)
        return primary_permissions.has_delete_permission
    except (models.ObjectDoesNotExist, TypeError):
        group = get_user_group(obj=obj, user=user)
        return object_permissions.deletebility_level >= group


def get_available_objects(
        model: type[models.Model],
        user: User,
        has_permission_field: str,
        level_field: str,
        owner_group: int = settings.OWNERS_GROUP,
):
    group = get_user_group(user=user)
    permissions_field = get_permissions_field(model)
    owner_field = get_owner_field(model)

    conditions = Q(
        **{f"{permissions_field}__user_permissions__{has_permission_field}": True},
        **{f"{permissions_field}__user_permissions__user": user}
    ) | Q(
        **{
            owner_field: user,
            f"{permissions_field}__{level_field}": owner_group,
        }
    ) | Q(
        **{f"{permissions_field}__{level_field}__gte": group}
    )

    queryset = model.objects.filter(conditions)

    exclude_conditions = Q(
        **{f"{permissions_field}__user_permissions__{has_permission_field}": False},
        **{f"{permissions_field}__user_permissions__user": user}
    )
    queryset = queryset.exclude(exclude_conditions)

    return queryset.distinct()


def get_visible_objects(user: User, model: type[models.Model]) -> QuerySet[models.Model]:
    return get_available_objects(
        model=model,
        user=user,
        has_permission_field="has_view_permission",
        level_field="visibility_level",
    )


def get_changeble_objects(user: User, model: type[models.Model]) -> QuerySet[models.Model]:
    return get_available_objects(
        model=model,
        user=user,
        has_permission_field="has_change_permission",
        level_field="changebility_level",
    )


def get_deleteble_objects(user: User, model: type[models.Model]) -> QuerySet[models.Model]:
    return get_available_objects(
        model=model,
        user=user,
        has_permission_field="has_delete_permission",
        level_field="deletebility_level",
    )
