from django.contrib.auth import get_user_model
from django.db import models

from src.apps.abandoned.models import AbandonedObject
from src.utils.db import get_all_objects, filter_objects

User = get_user_model()


def get_all_abandoned_objects() -> models.QuerySet[AbandonedObject]:
    return get_all_objects(AbandonedObject)


def get_unhidden_abandoned_objects() -> models.QuerySet[AbandonedObject]:
    return filter_objects(AbandonedObject, is_hidden=False)


def get_user_abandoned_objects(user: User) -> models.QuerySet[AbandonedObject]:
    return filter_objects(AbandonedObject, creator=user)
