from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from src.apps.abandoned.models.constants import (
    AREA_NAME_MAX_LENGTH,
    SECURITY_LEVEL_LENGTH,
)
from src.apps.abandoned.enums import SecurityLevel

User = get_user_model()


class AbandonedArea(models.Model):
    class Meta:
        verbose_name = _("Area")
        verbose_name_plural = _("Areas")

    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        help_text=_("Object creation date and time."),
        default=timezone.now,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        help_text=_("Object updated date and time."),
        auto_now=True,
    )
    area = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="areas",
        null=True,
        blank=True,
        verbose_name=_("Parent Area"),
        help_text=_("Area that contains current area."),
    )
    name = models.CharField(
        max_length=AREA_NAME_MAX_LENGTH,
        verbose_name=_("Name"),
        help_text=_("Name of the abandoned area."),
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Description of the abandoned area."),
        null=True,
        blank=True,
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="areas",
        blank=True,
        null=True,
        verbose_name=_("Creator"),
        help_text=_(""),
    )
    security_level = models.CharField(
        max_length=SECURITY_LEVEL_LENGTH,
        choices=SecurityLevel,
        default=SecurityLevel.NONE,
        null=False,
        blank=False,
        verbose_name=_("Security Level"),
        help_text=_("Security level of the area."),
    )

    def __str__(self):
        return f"Area(name={self.name})"
