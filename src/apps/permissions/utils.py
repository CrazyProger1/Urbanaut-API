import logging

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


def get_permissions_field(model: type[models.Model]) -> str:
    return getattr(model._meta, "permissions_field", "permissions")


def get_owner_field(model: type[models.Model]) -> str:
    return getattr(model._meta, "owner_field", "created_by")


def get_owner(obj: models.Model) -> User:
    return getattr(obj, get_owner_field(model=type(obj)), None)


def is_owner(obj: models.Model, user: User) -> bool:
    if not user or not obj:
        return False
    return get_owner(obj=obj) == user


def get_user_group(obj: models.Model = None, user: User = None):
    if user is None:
        return 400
    if user.is_superuser:
        return 0
    elif user.is_staff:
        return 100
    elif is_owner(obj, user):
        return 200
    elif user.is_authenticated:
        return 300
    return 400
