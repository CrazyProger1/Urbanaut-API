from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from src.apps.abandoned.models.enums import ParticipationStatus

User = get_user_model()


class Participation(models.Model):
    class Meta:
        verbose_name = _("Participation")
        verbose_name_plural = _("Participations")

    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        verbose_name=_("Event"),
        help_text=_(""),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="participations",
        blank=False,
        null=False,
        verbose_name=_("User"),
        help_text=_(""),
    )
    status = models.CharField(
        max_length=100,
        choices=ParticipationStatus,
        default=ParticipationStatus.REQUESTED,
        blank=False,
        null=False,
    )
