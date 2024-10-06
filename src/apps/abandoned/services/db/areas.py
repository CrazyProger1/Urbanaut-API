from django.contrib.auth import get_user_model
from django.db import models

from src.apps.abandoned.models import AbandonedArea
from src.utils.db import get_all_objects, filter_objects

User = get_user_model()


def get_all_abandoned_areas() -> models.QuerySet[AbandonedArea]:
    return get_all_objects(AbandonedArea)


def get_unhidden_abandoned_areas() -> models.QuerySet[AbandonedArea]:
    return filter_objects(AbandonedArea, is_hidden=False)


def get_user_abandoned_areas(user: User) -> models.QuerySet[AbandonedArea]:
    return filter_objects(AbandonedArea, creator=user)
