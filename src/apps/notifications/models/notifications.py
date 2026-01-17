from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.django.db import CreatedAtMixin


class Notification(CreatedAtMixin, models.Model):
    title = models.CharField(
        max_length=250,
        blank=False,
        null=False,
    )
    content = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("content"),
        help_text=_("Notification content."),
    )
    providers = models.ManyToManyField(
        to="NotificationProvider",
        related_name="notifications",
        blank=False,
    )
    recipients = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        blank=True,
        through="NotificationRecipient",
    )
    triggered_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("trigger at"),
        help_text=_("Notification should be shown at date and time."),
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="notifications",
    )
    is_shown = models.BooleanField(
        default=False,
        blank=False,
        null=False,
        verbose_name=_("is shown"),
        help_text=_("Was this notification shown?"),
    )

    def __str__(self):
        return self.title
