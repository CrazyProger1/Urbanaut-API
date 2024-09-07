from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.enums import NotificationType, NotificationIcon


class NotificationStatus(models.Model):
    class Meta:
        verbose_name = _("Notification Status")
        verbose_name_plural = _("Notification Statuses")
        unique_together = ("user", "notification")

    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("Recipient"),
        help_text=_(""),
    )
    notification = models.ForeignKey(
        "Notification",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("Notification"),
        help_text=_(""),
    )
    is_read = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        verbose_name=_("Read"),
        help_text=_(""),
    )

    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"


class Notification(models.Model):
    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")

    show_at = models.DateTimeField(
        null=False,
        blank=False,
        default=timezone.now,
        verbose_name=_("Show At"),
        help_text=_("Planned time to show."),
    )
    is_shown = models.BooleanField(
        default=False,
        blank=False,
        null=False,
        verbose_name=_("Shown"),
        help_text=_("Notification is already shown."),
    )
    recipients = models.ManyToManyField(
        "User",
        through=NotificationStatus,
        verbose_name=_("Recipients"),
        help_text=_(""),
    )
    title = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name=_("Title"),
        help_text=_(""),
    )
    message = models.TextField(
        blank=False,
        null=False,
        verbose_name=_("Message"),
        help_text=_(""),
    )
    type = models.CharField(
        choices=NotificationType,
        default=NotificationType.SYSTEM,
        null=False,
        blank=False,
        verbose_name=_("Type"),
        help_text=_("Type of the notification."),
    )
    icon = models.CharField(
        choices=NotificationIcon,
        default=NotificationIcon.NOTIFICATION,
        null=False,
        blank=False,
        verbose_name=_("Icon"),
        help_text=_("Icon of the notification."),
    )

    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"
