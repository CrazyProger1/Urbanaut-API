from django.contrib.auth import get_user_model
from django.db import models

from src.apps.abandoned.models import AbandonedObjectCategory

User = get_user_model()


def get_available_abandoned_object_categories(user: User = None) -> models.QuerySet[AbandonedObjectCategory]:
    return AbandonedObjectCategory.objects.visible(user=user)


def get_available_abandoned_object_category_children(category: AbandonedObjectCategory, user: User = None) -> models.QuerySet[
    AbandonedObjectCategory]:
    return category.children.visible(user=user)
