from django.contrib.auth import get_user_model

from src.utils.db import get_all_objects

User = get_user_model()


def get_all_users():
    return get_all_objects(User)
