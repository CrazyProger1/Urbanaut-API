import logging

from django.db import models
from django.db.models.enums import ChoicesType

logger = logging.getLogger(__name__)


class DynamicChoicesType(ChoicesType):
    __registered_names = []
    __registered_values = []
    __registered_labels = []

    def register(cls, name: str, value: str, label: str = None):
        label = label or name.replace("_", " ").title()
        logger.info(
            f"Dynamic choice registered: {cls.__name__}.{name} = {value}, {label}"
        )
        cls.__registered_labels.append(label)
        cls.__registered_values.append(value)
        cls.__registered_names.append(name)
        setattr(cls, name, value)

    @property
    def names(cls):
        return super().names + cls.__registered_names

    @property
    def choices(cls):
        choices = super().choices + list(
            zip(cls.__registered_values, cls.__registered_labels)
        )
        logger.info(f"Choices method called: {choices}")
        return choices


class DynamicTextChoices(models.TextChoices, metaclass=DynamicChoicesType):
    pass
