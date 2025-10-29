import logging

from django.db import models

from src.utils.django.db.types import (
    Model,
    Source,
)

logger = logging.getLogger(__name__)


def get_manager(
        model: type[models.Model],
        manager: str = "objects",
) -> models.Manager:
    manager_instance = getattr(model, manager, None)

    if manager_instance is None:
        raise AttributeError(f"No manager named '{manager}' found in {model.__name__}")

    if not isinstance(manager_instance, models.Manager):
        raise ValueError(
            f"'{manager}' in {model.__name__} must be an instance of models.Manager"
        )

    return manager_instance


def get_queryset(
        source: Source[Model],
        manager: str = "objects",
) -> models.QuerySet[Model]:
    if isinstance(source, models.QuerySet):
        return source
    elif isinstance(source, models.Manager):
        return source.get_queryset()
    else:
        return get_manager(model=source, manager=manager).get_queryset()
