from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.feedbacks.enums import RequestType
from src.utils.django.db import CreatedAtMixin


class Request(CreatedAtMixin, models.Model):
    comment = models.TextField(
        verbose_name=_("comment"),
        blank=True,
        null=True,
        help_text=_("Executor's comment related to the request."),
    )
    type = models.CharField(
        choices=RequestType,
        default=RequestType.OTHER,
        max_length=20,
        null=False,
        blank=False,
        help_text=_("Type of the request."),
    )
    path = models.CharField(
        verbose_name=_("path"),
        help_text=_("User path."),
        max_length=255,
        blank=True,
        null=True,
    )
    context = models.JSONField(
        verbose_name=_("context"),
        blank=False,
        null=False,
        help_text=_("Context of the request."),
    )
    is_fulfilled = models.BooleanField(
        verbose_name=_("is fulfilled"),
        default=False,
        blank=False,
        null=False,
    )
    requested_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name=_("requested by"),
        help_text=_("User who requested the request."),
        related_name="requests_requested",
        blank=True,
        null=True,
    )
    fulfilled_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name=_("fulfilled by"),
        help_text=_("Executor who fulfilled the request."),
        related_name="requests_fulfilled",
        blank=True,
        null=True,
    )
    fulfilled_at = models.DateTimeField(
        verbose_name=_("fulfilled at"),
        blank=True,
        null=True,
        help_text=_("Date and time at which the request was fulfilled."),
    )
