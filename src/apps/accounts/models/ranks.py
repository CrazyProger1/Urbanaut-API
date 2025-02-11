from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.db.models import TimestampModelMixin


class Rank(TimestampModelMixin, models.Model):
    key = models.CharField(
        max_length=20,
        unique=True,
        blank=False,
        null=False,
    )
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name=_("name"),
        help_text=_("The name of the rank."),
    )

    class Meta:
        verbose_name = _("Rank")
        verbose_name_plural = _("Ranks")

    def __str__(self):
        return f"{type(self).__name__}(name={self.name})"
