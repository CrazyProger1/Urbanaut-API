from django.db import models
from django.utils.translation import gettext_lazy as _


class FileType(models.TextChoices):
    PHOTO = "PHOTO", _("Photo")
    VIDEO = "VIDEO", _("Video")
    AUDIO = "AUDIO", _("Audio")
    DOCUMENT = "DOCUMENT", _("Document")
    EXECUTABLE = "EXECUTABLE", _("Executable")
    OTHER = "OTHER", _("Other")
