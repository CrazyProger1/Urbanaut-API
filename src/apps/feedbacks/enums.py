from django.db import models
from django.utils.translation import gettext_lazy as _


class RequestType(models.TextChoices):
    CORRECTION = "CORRECTION", _("Correction")
    COMPLAINT = "COMPLAINT", _("Complaint")
    OTHER = "OTHER", _("Other")
