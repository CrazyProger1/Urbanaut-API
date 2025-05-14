from django.contrib.auth import get_user_model

from src.apps.media.models import File
from src.utils.db import get_all_objects, filter_objects, create_object

User = get_user_model()


def get_all_files():
    return get_all_objects(File)


def get_unhidden_files():
    return filter_objects(File, is_hidden=False)


def get_user_files(user: User):
    return filter_objects(File, created_by=user)


def create_file(**data) -> File:
    return create_object(
        source=File,
        **data,
    )
