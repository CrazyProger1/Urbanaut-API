from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class TimestampModelMixin(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        help_text=_("Creation date and time."),
        default=timezone.now,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        help_text=_("Update date and time."),
        auto_now=True,
    )

    class Meta:
        abstract = True
