from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class File(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        help_text=_("File creation date and time."),
        default=timezone.now,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        help_text=_("File updated date and time."),
        auto_now=True,
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="files",
        blank=True,
        null=True,
        verbose_name=_("Creator"),
        help_text=_(""),
    )
    file = models.FileField(
        upload_to=settings.UPLOAD_DIR,
        blank=False,
        null=False,
        verbose_name=_("File"),
        help_text=_("Uploaded file."),
    )
