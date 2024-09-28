from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from src.apps.media.enums import FileType

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
        help_text=_("User who uploaded the file."),
    )
    file = models.FileField(
        upload_to=settings.UPLOAD_DIR,
        blank=False,
        null=False,
        verbose_name=_("File"),
        help_text=_("Uploaded file."),
    )
    type = models.CharField(
        choices=FileType,
        default=FileType.OTHER,
        verbose_name=_("Type"),
        help_text=_("File type."),
        blank=False,
        null=False,
    )
    is_hidden = models.BooleanField(
        verbose_name=_("Hidden"),
        help_text=_("Hidden from general users and available only for admins and creator."),
        default=False,
        null=False,
        blank=False,
    )

    @property
    def url(self) -> str | None:
        if self.pk:
            return reverse(
                "file-download",
                args=(self.pk,),
            )

    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"
