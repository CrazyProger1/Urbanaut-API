from typing import Iterable

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet

from src.apps.abandoned.models import AbandonedObject
from src.utils.db import search_localized

User = get_user_model()


def get_available_abandoned_objects(user: User = None) -> models.QuerySet[AbandonedObject]:
    return AbandonedObject.objects.visible(user=user)


def search_abandoned_objects(
        queryset: QuerySet[AbandonedObject],
        term: str,
        fields: Iterable[str] = ("name", "description"),
) -> models.QuerySet[AbandonedObject]:
    return search_localized(
        queryset=queryset,
        term=term,
        fields=fields,
    )
