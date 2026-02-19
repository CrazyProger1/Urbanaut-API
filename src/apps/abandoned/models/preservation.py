from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

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
    has_roof = models.BooleanField(
        default=False,
        verbose_name=_("has roof"),
        help_text=_("Has roof?"),
        blank=False,
        null=False,
    )
    has_walls = models.BooleanField(
        default=False,
        verbose_name=_("has walls"),
        help_text=_("Has walls?"),
        blank=False,
        null=False,
    )
    has_floor = models.BooleanField(
        default=False,
        verbose_name=_("has floor"),
        help_text=_("Has floor?"),
        blank=False,
        null=False,
    )
    has_windows = models.BooleanField(
        default=False,
        verbose_name=_("has windows"),
        help_text=_("Has windows?"),
        blank=False,
        null=False,
    )
    has_internal_ceilings = models.BooleanField(
        default=False,
        verbose_name=_("has internal ceilings"),
        help_text=_("Has internal ceilings?"),
        blank=False,
        null=False,
    )
    has_doors = models.BooleanField(
        default=False,
        verbose_name=_("has doors"),
        help_text=_("Has doors?"),
        blank=False,
        null=False,
    )

    @property
    def actual_level(self) -> PreservationLevel:
        score = 0

        for factor, weight in settings.PRESERVATION_LEVEL_WEIGHTS_LOOKUP.items():
            if getattr(self, factor, False):
                score += weight

        for score_range, level in settings.PRESERVATION_LEVEL_LOOKUP.items():
            min_score, max_score = score_range

            if min_score <= score <= max_score:
                return level

        return PreservationLevel.NONE

    def _update_level(self):
        self.level = self.actual_level
        self.save(update_fields=("level",))

    def save(
            self,
            *args,
            **kwargs,
    ):
        super().save(*args, **kwargs)

        if "level" not in kwargs.get("update_fields", ()):
            self._update_level()

    def __str__(self):
        return f"Preservation of {self.place}: {self.level}"
