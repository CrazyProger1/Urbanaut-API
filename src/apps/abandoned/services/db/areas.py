from django.contrib.auth import get_user_model
from django.db import models

from src.apps.abandoned.models import AbandonedArea
from src.utils.db import get_all_objects, filter_objects

User = get_user_model()


def get_available_abandoned_areas(user: User = None) -> models.QuerySet[AbandonedArea]:
    return AbandonedArea.objects.visible(user=user)
