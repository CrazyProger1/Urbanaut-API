import logging

from django.db import models

from .types import Source

logger = logging.getLogger(__name__)


def get_manager(model: type[models.Model], manager: str = "objects") -> models.Manager:
    manager = getattr(model, manager, None)

    if not manager:
        raise AttributeError(f"No manager found at {model}")

    elif not isinstance(manager, models.Manager):
        raise ValueError(f"Manager must be an instance of {models.Manager} subclass")

    return manager


def get_queryset[
T: models.Model
](
        source: Source[T],
        manager: str = "objects",
) -> models.QuerySet[T]:
    if isinstance(source, models.QuerySet):
        return source
    elif issubclass(source, models.Manager):
        return source.get_queryset()
    else:
        return get_manager(
            model=source,
            manager=manager,
        ).get_queryset()


def create_object[
T: models.Model
](source: Source[T], manager: str = "objects", **data) -> T:
    queryset = get_queryset(
        source=source,
        manager=manager,
    )
    obj = queryset.create(**data)
    logger.debug(f"Object of type {source} inserted with {data}")
    return obj


def get_all_objects[
T: models.Model
](source: Source[T], manager: str = "objects") -> models.QuerySet[T]:
    queryset = get_queryset(
        source=source,
        manager=manager,
    )

    logger.debug(f"All objects of type {source} selected")
    return queryset


def filter_objects[
T: models.Model
](source: Source[T], *args, manager: str = "objects", **kwargs) -> models.QuerySet[T]:
    queryset = get_queryset(
        source=source,
        manager=manager,
    )

    resultset = queryset.filter(*args, **kwargs)
    logger.debug(f"Many objects of type {source} with {args} {kwargs} selected")
    return resultset


def get_object_or_error[
T: models.Model
](source: Source[T], *args, manager: str = "objects", **kwargs) -> T:
    queryset = get_queryset(
        source=source,
        manager=manager,
    )
    model = queryset.model
    try:

        obj = queryset.get(*args, **kwargs)
        logger.debug(f"Object of type {model} with {args} {kwargs} selected: {obj}")
        return obj
    except queryset.model.DoesNotExist:
        logger.warning(f"Object of type {model} with {args} {kwargs} not found")
        raise


def get_object_or_none[
T: models.Model
](source: Source[T], *args, manager: str = "objects", **kwargs) -> T | None:
    try:
        return get_object_or_error(
            source,
            *args,
            manager=manager,
            **kwargs,
        )
    except source.DoesNotExist:
        pass
