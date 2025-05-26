from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from src.utils.db import TimestampMixin


class Newsletter(TimestampMixin, models.Model):
    name = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name=_("internal name"),
        help_text=_("Internal name of the newsletter."),
    )
    message = models.TextField(
        blank=False,
        null=False,
        verbose_name=_("message"),
        help_text=_("Message of the newsletter."),
    )
    shown_at = models.DateTimeField(
        null=False,
        blank=False,
        default=timezone.now,
        verbose_name=_("shown at"),
        help_text=_("Time when the newsletter was shown."),
    )
    is_shown = models.BooleanField(
        default=False,
        blank=False,
        null=False,
        verbose_name=_("shown"),
        help_text=_("Newsletter is already shown."),
    )

    def __str__(self):
        return self.name
