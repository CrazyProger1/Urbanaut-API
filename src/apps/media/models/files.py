from urllib.parse import urljoin

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from src.apps.media.enums import FileType
from src.utils.db.models import TimestampMixin

User = get_user_model()


class File(TimestampMixin, models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="files",
        blank=True,
        null=True,
        verbose_name=_("created by"),
        help_text=_("User who uploaded the file."),
    )
    file = models.FileField(
        upload_to=settings.UPLOAD_DIR,
        blank=False,
        null=False,
        verbose_name=_("file"),
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
        help_text=_(
            "Hidden from general users and available only for admins and creator."
        ),
        default=False,
        null=False,
        blank=False,
    )

    @property
    def src(self) -> str | None:
        if self.pk:
            return urljoin(
                settings.BASE_URL,
                reverse(
                    "file-src",
                    args=(self.pk,),
                ),
            )

    def __str__(self):
        return f"{self.file.name}"
