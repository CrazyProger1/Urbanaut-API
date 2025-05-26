from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.db import CreatedAtMixin


class Friend(CreatedAtMixin, models.Model):
    initiator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_friend_requests",
        null=False,
        blank=False,
        verbose_name=_("initiator"),
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_friend_requests",
        null=False,
        blank=False,
        verbose_name=_("recipient"),
    )
    approved_at = models.DateTimeField(
        verbose_name=_("approved at"),
        help_text=_("Friendship request approving date and time."),
        null=True,
        blank=True,
    )
    is_approved = models.BooleanField(
        verbose_name=_("approved"),
        help_text=_("Friendship request has been approved."),
        default=False,
        null=False,
        blank=False,
    )
