from django.db import models
from django.utils.translation import gettext as _

from src.apps.abandoned.models.constants import OBJECT_NAME_MAX_LENGTH


class AbandonedObject(models.Model):
    class Meta:
        verbose_name = _("Object")
        verbose_name_plural = _("Objects")

    area = models.ForeignKey(
        "AbandonedArea",
        on_delete=models.CASCADE,
        related_name="objects",
        null=True,
        blank=True,
        verbose_name=_("Area"),
        help_text=_("Area that contains current object."),
    )
    name = models.CharField(
        max_length=OBJECT_NAME_MAX_LENGTH,
        verbose_name=_("Name"),
        help_text=_("Name of the abandoned object."),
        null=False,
        blank=False,
    )
