from django.db import models
from django.utils.translation import gettext_lazy as _


class Terms(models.Model):
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

    def __str__(self):
        return f"Terms of Usage V{self.version}"
