from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


def get_permissions_field(model: type[models.Model]) -> str:
    return getattr(model._meta, "permissions_field", "permissions")


def get_owner_field(model: type[models.Model]) -> str:
    return getattr(model._meta, "owner_field", "creator")


def get_owner(obj: models.Model) -> User:
    return getattr(obj, get_owner_field(model=type(obj)), None)


def is_owner(obj: models.Model, user: User) -> bool:
    if not user:
        return False
    return get_owner(obj=obj) == user
