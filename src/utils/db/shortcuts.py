import logging

from django.db import models

logger = logging.getLogger(__name__)


def get_manager(model: models.Model, manager: str = "objects") -> models.Manager:
    manager = getattr(model, manager, None)

    if not manager:
        raise AttributeError(f"No manager found at {model}")

    elif not isinstance(manager, models.Manager):
        raise ValueError(f"Manager must be an instance of {models.Manager} subclass")

    return manager


def create_object[
T: models.Model
](model: type[T], manager: str = "objects", **data) -> T:
    obj = get_manager(model=model, manager=manager).create(**data)
    logger.debug(f"Object of type {model} inserted with {data}")
    return obj


def get_all_objects[
T: models.Model
](model: type[T], manager: str = "objects") -> models.QuerySet[T]:
    queryset = get_manager(
        model=model,
        manager=manager,
    ).all()

    logger.debug(f"All objects of type {model} selected")
    return queryset


def filter_objects[
T: models.Model
](model: type[T], *args, manager: str = "objects", **kwargs) -> models.QuerySet[T]:
    queryset = get_manager(
        model=model,
        manager=manager,
    ).filter(*args, **kwargs)

    logger.debug(f"Many objects of type {model} with {args} {kwargs} selected")
    return queryset


def get_object_or_error[
T: models.Model
](model: type[T], *args, manager: str = "objects", **kwargs) -> T:
    try:
        obj = get_manager(
            model=model,
            manager=manager,
        ).get(*args, **kwargs)
        logger.debug(f"Object of type {model} with {args} {kwargs} selected: {obj}")
        return obj
    except model.DoesNotExist:
        logger.warning(f"Object of type {model} with {args} {kwargs} not found")
        raise


def get_object_or_none[
T: models.Model
](model: type[T], *args, manager: str = "objects", **kwargs) -> T | None:
    try:
        return get_object_or_error(
            model=model,
            manager=manager,
            *args,
            **kwargs,
        )
    except model.DoesNotExist:
        pass
