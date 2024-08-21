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
    IN_PROCESS = "IN_PROCESS", _("IN PROCESS")
    FINISHED = "FINISHED", _("FINISHED")
    CANCELLED = "CANCELLED", _("CANCELLED")


class SecurityLevel(models.TextChoices):
    NONE = "NONE", _("NONE")


class PreservationLevel(models.TextChoices):
    LOW = "LOW", _("LOW")
    MEDIUM = "MEDIUM", _("MEDIUM")
    HIGH = "HIGH", _("HIGH")
    DANGEROUS = "DANGEROUS", _("DANGEROUS")


class DifficultyLevel(models.TextChoices):
    NEWBIE = "NEWBIE", _("NEWBIE")
    EASY = "EASY", _("EASY")
    MEDIUM = "MEDIUM", _("MEDIUM")
    HIGH = "HIGH", _("HIGH")
