from django.db import models

from src.apps.abandoned.models import AbandonedObject
from src.utils.db import get_all_objects


def get_all_abandoned_objects() -> models.QuerySet[AbandonedObject]:
    return get_all_objects(AbandonedObject)
