from django.db import models
from django.utils.translation import gettext_lazy as _


class FileType(models.TextChoices):
    PHOTO = "PHOTO", _("PHOTO")
    VIDEO = "VIDEO", _("VIDEO")
    AUDIO = "AUDIO", _("AUDIO")
    DOCUMENT = "DOCUMENT", _("DOCUMENT")
    EXECUTABLE = "EXECUTABLE", _("EXECUTABLE")
    OTHER = "OTHER", _("OTHER")
