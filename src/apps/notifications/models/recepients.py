from heapq import nlargest

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class NotificationRecipient(models.Model):
    class Meta:
        unique_together = (
            "user",
            "notification",
        )

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    notification = models.ForeignKey(
        to="Notification",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name=_("is read"),
        help_text=_("User read message."),
        null=False,
        blank=False,
    )
    read_at = models.DateTimeField(
        verbose_name=_("read at"),
        help_text=_("User read message at date and time."),
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.user)
