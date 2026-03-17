from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from src.apps.expeditions.enums import ExpeditionState
from src.utils.django.db import TimestampMixin


class Expedition(TimestampMixin, models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name=_("name"),
        help_text=_("Name of the expedition."),
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Description of the expedition."),
        null=True,
        blank=True,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="expeditions",
    )
    started_at = models.DateTimeField(
        verbose_name=_("start at"),
        help_text=_("Start date and time (planned or actual)."),
        null=True,
        blank=True,
    )
    ended_at = models.DateTimeField(
        verbose_name=_("ended at"),
        help_text=_("End date and time (planned or actual or cancel)."),
        null=True,
        blank=True,
    )
    state = models.CharField(
        choices=ExpeditionState,
        default=ExpeditionState.PLANNED,
        verbose_name=_("state"),
        help_text=_("State of the expedition."),
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = _("Expedition")
        verbose_name_plural = _("Expeditions")
