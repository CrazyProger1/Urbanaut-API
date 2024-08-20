from django.db import models
from django.utils.translation import gettext as _

from src.apps.abandoned.models.constants import AREA_NAME_MAX_LENGTH


class AbandonedArea(models.Model):
    class Meta:
        verbose_name = _("Area")
        verbose_name_plural = _("Areas")

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
