from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.db import TimestampModelMixin


class Newsletter(TimestampModelMixin, models.Model):
    name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name=_("internal name"),
        help_text=_("Internal name of the newsletter."),
    )
    message = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("message"),
        help_text=_("Message of the newsletter."),
    )

    def __str__(self):
        return self.name
