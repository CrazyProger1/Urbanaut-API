from django.db import models

from src.apps.accounts.models import Settings
from src.utils.db import get_all_objects


def get_user_settings(user) -> Settings:
    return user.settings


def get_all_settings() -> models.QuerySet[Settings]:
    return get_all_objects(source=Settings)
