from django.db import models
from django.utils.translation import gettext_lazy as _


class ExpeditionState(models.TextChoices):
    PLANNED = "PLANNED", _("Planned")
    IN_PROCESS = "IN_PROCESS", _("In process")
    FINISHED = "FINISHED", _("Finished")
    CANCELLED = "CANCELLED", _("Cancelled")


class ParticipationState(models.TextChoices):
    REQUESTED = "REQUESTED", _("Requested")
    PLANNED = "PLANNED", _("Planned")
    PARTICIPATED = "PARTICIPATED", _("Participated")


class WaypointType(models.TextChoices):
    POI = "POI", _("POI")
    MEETING = "MEETING", _("Meeting")
