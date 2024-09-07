from django.db import models

from src.apps.abandoned.models import AbandonedArea
from src.utils.db import get_all_objects


def get_all_abandoned_areas() -> models.QuerySet[AbandonedArea]:
    return get_all_objects(AbandonedArea)
