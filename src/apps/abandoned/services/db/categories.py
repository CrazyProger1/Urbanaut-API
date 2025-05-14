from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet

from src.apps.abandoned.models import Category

User = get_user_model()


def get_available_abandoned_object_categories(
    user: User = None,
) -> models.QuerySet[Category]:
    return Category.objects.visible(user=user)


def get_available_abandoned_object_category_children(
    category: Category, user: User = None
) -> models.QuerySet[Category]:
    return category.children.visible(user=user)


def get_available_toplevel_abandoned_object_categories(
    user: User = None,
) -> QuerySet[Category]:
    return Category.objects.visible(user=user).filter(parent=None)
