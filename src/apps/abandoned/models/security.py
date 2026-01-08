from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.abandoned.enums import SecurityLevel


class PlaceSecurity(models.Model):
    """
    TODO:
    - security type - Private Security Company, Military, so on...
    - know security points (booth, rooms, so on...)
    """

    place = models.OneToOneField(
        "Place",
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="security",
    )
    level = models.CharField(
        max_length=10,
        choices=SecurityLevel,
        default=SecurityLevel.NONE,
        verbose_name=_("level"),
        help_text=_("Current security level based on community feedbacks."),
    )

    def __str__(self):
        return self.place.name
