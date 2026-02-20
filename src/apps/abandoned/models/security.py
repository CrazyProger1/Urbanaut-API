from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.abandoned.enums import SecurityLevel


class PlaceSecurity(models.Model):
    """
    Doubts about the legality
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
    has_security = models.BooleanField(
        default=False,
        verbose_name=_("security"),
        help_text=_("Has security?"),
        blank=False,
        null=False,
    )

    has_dogs = models.BooleanField(
        default=False,
        verbose_name=_("dogs"),
        help_text=_("Has dogs?"),
        blank=False,
        null=False,
    )
    has_weapons = models.BooleanField(
        default=False,
        verbose_name=_("weapons"),
        help_text=_("Has weapons?"),
        blank=False,
        null=False,
    )
    has_cameras = models.BooleanField(
        default=False,
        verbose_name=_("cameras"),
        help_text=_("Has cameras?"),
        blank=False,
        null=False,
    )
    has_sensors = models.BooleanField(
        default=False,
        verbose_name=_("sensors"),
        help_text=_("Has sensors?"),
        blank=False,
        null=False,
    )

    @property
    def actual_level(self) -> SecurityLevel:
        score = 0

        if not self.has_security:
            return SecurityLevel.NONE

        for factor, weight in settings.SECURITY_LEVEL_WEIGHTS_LOOKUP.items():
            if getattr(self, factor, False):
                score += weight

        for score_range, level in settings.SECURITY_LEVEL_LOOKUP.items():
            min_score, max_score = score_range

            if min_score <= score <= max_score:
                return level

        return SecurityLevel.NONE

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
        return f"Security of {self.place}: {self.has_security}"
