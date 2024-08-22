from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from src.apps.abandoned.models.constants import EVENT_NAME_MAX_LENGTH
from src.apps.abandoned.models.enums import EventStatus

User = get_user_model()


class Event(models.Model):
    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    name = models.CharField(
        max_length=EVENT_NAME_MAX_LENGTH,
        verbose_name=_("Name"),
        help_text=_("Name of the event."),
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At"),
        help_text=_("Event creation date and time."),
    )
    start_datetime = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name=_("Start Datetime"),
        help_text=_("Date and time of start of trip."),
    )

    end_datetime = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name=_("End Datetime"),
        help_text=_("Date and time of end of trip."),
    )

    participants = models.ManyToManyField(
        User,
        related_name="events",
        verbose_name=_("Participants"),
        help_text=_("Users that participate in this trip."),
        through="Participation",
    )
    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="my_events",
        blank=False,
        null=False,
        verbose_name=_("Organizer"),
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
