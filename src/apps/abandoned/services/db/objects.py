from typing import Iterable

from django.contrib.auth import get_user_model
from django.db import models

from src.apps.abandoned.models import AbandonedObject
from src.utils.db import search_localized
from src.utils.db.types import Source

User = get_user_model()


def get_available_abandoned_objects(user: User = None) -> models.QuerySet[AbandonedObject]:
    return AbandonedObject.objects.visible(user=user)


def search_abandoned_objects(
        source: Source[AbandonedObject],
        term: str,
        fields: Iterable[str] = ("name", "description"),
) -> models.QuerySet[AbandonedObject]:
    return search_localized(
        source=source,
        term=term,
        fields=fields,
    )
