from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class NotificationStatus(models.Model):
    class Meta:
        verbose_name = _("Notification Status")
        verbose_name_plural = _("Notification Statuses")
        unique_together = ("user", "notification")

    user = models.ForeignKey(
        User,
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
