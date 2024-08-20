from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

User = get_user_model()


class AttendanceReport(models.Model):
    class Meta:
        verbose_name = _("Report")
        verbose_name_plural = _("Reports")

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Created At"),
        help_text=_("Report creation date and time."),
    )
    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        related_name="reports",
        verbose_name=_("Event"),
        help_text=_("Report destination event."),
    )
