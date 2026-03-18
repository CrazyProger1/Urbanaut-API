from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.expeditions.models.participations import Participation
from src.utils.django.db import TimestampMixin


class Report(TimestampMixin, models.Model):
    participation = models.OneToOneField(
        to=Participation,
        on_delete=models.CASCADE,
        related_name="report",
    )
    summary = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("summary"),
        help_text=_("Summary of the expedition from participant's point of view."),
    )
    is_confirmed = models.BooleanField(
        default=False,
        verbose_name=_("is confirmed"),
        help_text=_("Participant surely took part in the expedition."),
    )
