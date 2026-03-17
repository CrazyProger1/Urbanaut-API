from django.db import models
from django.utils.translation import gettext_lazy as _


class ExpeditionState(models.TextChoices):
    PLANNED = "PLANNED", _("Planned")
    IN_PROCESS = "IN_PROCESS", _("In process")
    FINISHED = "FINISHED", _("Finished")
    CANCELLED = "CANCELLED", _("Cancelled")
