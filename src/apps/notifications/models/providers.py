from django.db import models

from src.apps.notifications.enums import (
    NotificationProvider as PhysicalNotificationProvider,
)
from django.utils.translation import gettext_lazy as _


class NotificationProvider(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name=_("name"),
        help_text=_("Name of the provider."),
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Description of the provider."),
        null=True,
        blank=True,
    )
    physical_provider = models.CharField(
        choices=PhysicalNotificationProvider,
        verbose_name=_("physical provider"),
        help_text=_("Physically implemented provider."),
        max_length=20,
        default=PhysicalNotificationProvider.WEBSITE,
        blank=False,
        null=False,
    )
    is_enabled = models.BooleanField(
        verbose_name=_("is enabled"),
        default=True,
        name=False,
        blank=False,
    )

    class Meta:
        verbose_name = _("Provider")
        verbose_name_plural = _("Providers")

    def __str__(self):
        return self.name
