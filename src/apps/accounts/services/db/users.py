from django.contrib.auth import get_user_model

from src.utils.db import get_all_objects, get_object_or_none

User = get_user_model()


def get_all_users():
    return get_all_objects(User)


def get_user_or_none(*args, **kwargs):
    return get_object_or_none(
        User,
        *args,
        **kwargs,
    )


def get_user_or_create(**data) -> User | None:
    try:
        return User.objects.get(**data)
    except User.DoesNotExist:
        return User.objects.create_user(**data)
