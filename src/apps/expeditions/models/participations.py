from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.expeditions.enums import ParticipationState
from src.apps.expeditions.models import Expedition
from src.utils.django.db import CreatedAtMixin


class Participation(CreatedAtMixin, models.Model):
    expedition = models.ForeignKey(
        to=Expedition,
        on_delete=models.CASCADE,
        related_name="participations",
    )
    participant = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="participations",
        null=True,
        blank=True,
    )
    state = models.CharField(
        verbose_name=_("state"),
        choices=ParticipationState,
        default=ParticipationState.PLANNED,
    )

    class Meta:
        verbose_name = _("Participation")
        verbose_name_plural = _("Participations")
