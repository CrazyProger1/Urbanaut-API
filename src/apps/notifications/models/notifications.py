from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from src.apps.notifications.enums import NotificationType, NotificationIcon
from src.apps.notifications.models.statuses import NotificationStatus

User = get_user_model()


class Notification(models.Model):
    class Meta:
        verbose_name = _("notification")
        verbose_name_plural = _("notifications")

    show_at = models.DateTimeField(
        null=False,
        blank=False,
        default=timezone.now,
        verbose_name=_("show at"),
        help_text=_("Planned time to show."),
    )
    is_shown = models.BooleanField(
        default=False,
        blank=False,
        null=False,
        verbose_name=_("shown"),
        help_text=_("Notification is already shown."),
    )
    recipients = models.ManyToManyField(
        User,
        through=NotificationStatus,
        verbose_name=_("recipients"),
        help_text=_("Recipients of the notification."),
    )
    title = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name=_("title"),
        help_text=_(""),
    )
    message = models.TextField(
        blank=False,
        null=False,
        verbose_name=_("message"),
        help_text=_("Message of the notification."),
    )
    type = models.CharField(
        choices=NotificationType,
        default=NotificationType.SYSTEM,
        null=False,
        blank=False,
        verbose_name=_("type"),
        help_text=_("Type of the notification."),
    )
    icon = models.CharField(
        choices=NotificationIcon,
        default=NotificationIcon.NOTIFICATION,
        null=False,
        blank=False,
        verbose_name=_("icon"),
        help_text=_("Icon of the notification."),
    )

    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"
