from django.db import models
from django.utils.translation import gettext as _


class ParticipationStatus(models.TextChoices):
    REQUESTED = "REQUESTED", _("REQUESTED")
    PLANNED = "PLANNED", _("PLANNED")
    PARTICIPATED = "PARTICIPATED", _("PARTICIPATED")
    CONFIRMED = "CONFIRMED", _("CONFIRMED")
    CANCELLED = "CANCELLED", _("CANCELLED")


class EventStatus(models.TextChoices):
    PLANNED = "PLANNED", _("PLANNED")
    FINISHED = "FINISHED", _("FINISHED")
    CANCELLED = "CANCELLED", _("CANCELLED")
