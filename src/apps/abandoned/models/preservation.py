from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.abandoned.enums import PreservationLevel


class PlacePreservation(models.Model):
    place = models.OneToOneField(
        "Place",
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="preservation",
    )
    level = models.CharField(
        max_length=10,
        choices=PreservationLevel,
        default=PreservationLevel.MEDIUM,
        verbose_name=_("level"),
        help_text=_("Current preservation level based on community feedbacks."),
    )
