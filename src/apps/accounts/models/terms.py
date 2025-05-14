from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.db import TimestampModelMixin


class Terms(models.Model, TimestampModelMixin):
    class Meta:
        verbose_name = _("Terms of Usage")
        verbose_name_plural = _("Terms of Usage")

    is_active = models.BooleanField(
        verbose_name=_("active"),
        help_text=_("Active version of Terms of Usage."),
        default=False,
        blank=False,
        null=False,
    )

    version = models.CharField(
        verbose_name=_("version"),
        help_text=_("Version of Terms of Usage."),
        blank=False,
        null=False,
        default="0.0.1",
        unique=True,
    )
    content = models.CharField(
        verbose_name=_("content"),
        help_text=_("Content of Terms of Usage."),
        blank=False,
        null=False,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="terms",
        blank=True,
        null=True,
        verbose_name=_("created by"),
        help_text=_("User-author of this version of Terms of Usage."),
    )

    def __str__(self):
        return f"Terms of Usage V{self.version}"
