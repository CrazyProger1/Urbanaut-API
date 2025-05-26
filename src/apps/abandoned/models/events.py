from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.abandoned.enums import EventStatus
from src.apps.permissions.models import PermissionBaseModel
from src.utils.db.models import TimestampMixin

User = get_user_model()


class Event(TimestampMixin, PermissionBaseModel):
    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")

    name = models.CharField(
        max_length=250,
        verbose_name=_("name"),
        help_text=_("Name of the event."),
        null=False,
        blank=False,
    )
    short_description = models.CharField(
        verbose_name=_("short description"),
        help_text=_("Short description of the event for the events page."),
        null=False,
        blank=False,
    )
    start_at = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name=_("start at"),
        help_text=_("Date and time of start of trip."),
    )

    end_at = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name=_("end at"),
        help_text=_("Date and time of end of trip."),
    )
    participants = models.ManyToManyField(
        User,
        related_name="events",
        verbose_name=_("participants"),
        help_text=_("Users that participate in this trip."),
        through="Participation",
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="my_events",
        blank=False,
        null=False,
        verbose_name=_("organizer"),
        help_text=_(""),
    )
    status = models.CharField(
        max_length=100,
        choices=EventStatus,
        default=EventStatus.PLANNED,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"Event(name={self.name})"
