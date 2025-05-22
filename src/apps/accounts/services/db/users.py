from django.contrib.auth import get_user_model

from src.apps.accounts.services.db.ranks import get_default_rank
from src.utils.db import get_all_objects, get_object_or_none, Source, filter_objects

User = get_user_model()


def get_all_users():
    return get_all_objects(User)


def get_active_users(source: Source[User] = User):
    return filter_objects(source=source, is_active=True)


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
        if not data.get("rank"):
            data["rank"] = get_default_rank()
        return User.objects.create_user(**data)
