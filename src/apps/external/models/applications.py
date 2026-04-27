from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.django.db import TimestampMixin


class Application(TimestampMixin, models.Model):
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="applications",
    )
    name = models.CharField(
        verbose_name=_("name"),
        max_length=255,
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = _("Application")
        verbose_name_plural = _("Applications")

    def __str__(self):
        return f"{self.name} - {self.created_by}"
