from django.db import models

from src.apps.abandoned.models import AbandonedObject
from src.utils.db import get_all_objects, filter_objects


def get_all_abandoned_objects() -> models.QuerySet[AbandonedObject]:
    return get_all_objects(AbandonedObject)


def get_unhidden_abandoned_objects() -> models.QuerySet[AbandonedObject]:
    return filter_objects(AbandonedObject, is_hidden=False)
