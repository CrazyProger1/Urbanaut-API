from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.abandoned.enums import ParticipationStatus

User = get_user_model()


class Participation(models.Model):
    class Meta:
        verbose_name = _("participation")
        verbose_name_plural = _("participations")

    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        verbose_name=_("event"),
        help_text=_(""),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="participations",
        blank=False,
        null=False,
        verbose_name=_("user"),
        help_text=_(""),
    )
    status = models.CharField(
        max_length=100,
        choices=ParticipationStatus,
        default=ParticipationStatus.REQUESTED,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"Participation(event={self.event}, user={self.user})"
