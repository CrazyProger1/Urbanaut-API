from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.actions.enums import ActionType

ActionType.register("CREATED_ABANDONED_OBJECT", "CREATED ABANDONED OBJECT", _("CREATED ABANDONED OBJECT"))
ActionType.register("CREATED_ABANDONED_AREA", "CREATED ABANDONED AREA", _("CREATED ABANDONED AREA"))
ActionType.register("UPDATED_ABANDONED_OBJECT", "UPDATED ABANDONED OBJECT", _("UPDATED ABANDONED OBJECT"))
ActionType.register("UPDATED_ABANDONED_AREA", "UPDATED ABANDONED AREA", _("UPDATED ABANDONED AREA"))


class ParticipationStatus(models.TextChoices):
    REQUESTED = "REQUESTED", _("REQUESTED")
    PLANNED = "PLANNED", _("PLANNED")
    PARTICIPATED = "PARTICIPATED", _("PARTICIPATED")
    CONFIRMED = "CONFIRMED", _("CONFIRMED")
    CANCELLED = "CANCELLED", _("CANCELLED")


class EventStatus(models.TextChoices):
    PLANNED = "PLANNED", _("PLANNED")
    IN_PROCESS = "IN_PROCESS", _("IN PROCESS")
    FINISHED = "FINISHED", _("FINISHED")
    CANCELLED = "CANCELLED", _("CANCELLED")


class SecurityLevel(models.TextChoices):
    NO = "NO", _("NO")
    YES = "YES", _("YES")
    YES_WITH_DOGS = "YES_WITH_DOGS", _("YES WITH DOGS")
    YES_WITH_WEAPONS = "YES_WITH_WEAPONS", _("YES WITH WEAPONS")
    YES_MILITARY = "YES_MILITARY", _("YES_MILITARY")

class PreservationLevel(models.TextChoices):
    LOW = "LOW", _("LOW")
    MEDIUM = "MEDIUM", _("MEDIUM")
    HIGH = "HIGH", _("HIGH")
    DANGEROUS = "DANGEROUS", _("DANGEROUS")


class DifficultyLevel(models.TextChoices):
    NEWBIE = "NEWBIE", _("NEWBIE")
    EASY = "EASY", _("EASY")
    MEDIUM = "MEDIUM", _("MEDIUM")
    HARD = "HARD", _("HARD")
    LEGEND = "LEGEND", _("LEGEND")
