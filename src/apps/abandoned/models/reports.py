from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ParticipationReport(models.Model):
    class Meta:
        verbose_name = _("report")
        verbose_name_plural = _("reports")

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("created at"),
        help_text=_("Report creation date and time."),
    )
    participation = models.ForeignKey(
        "Participation",
        on_delete=models.CASCADE,
        related_name="reports",
        verbose_name=_("participation"),
        help_text=_("Report destination participation."),
    )

    def __str__(self):
        return f"Report(participation={self.participation})"
