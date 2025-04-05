from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.db import get_or_create_object


class Settings(models.Model):
    class Meta:
        verbose_name = _("Settings")
        verbose_name_plural = _("Settings")

    language = models.CharField(
        max_length=10,
        choices=settings.LANGUAGES,
        default="en",
        verbose_name=_("language"),
        help_text=_("Preferred language of the user."),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="settings",
        verbose_name=_("user"),
        help_text=_("User settings."),
    )
    timezone = models.CharField(
        max_length=50,
        choices=settings.TIME_ZONE_CHOICES,
        default="UTC",
        verbose_name=_("timezone"),
        help_text=_("Preferred timezone of the user."),
    )

    def __str__(self):
        return "Settings"


class SettingsUserMixin(models.Model):
    class Meta:
        abstract = True

    def create_settings_if_not_exists(self):
        get_or_create_object(
            source=Settings,
            user=self,
        )

    def save(
            self,
            *args,
            **kwargs,
    ):
        super().save(
            *args,
            **kwargs,
        )
        self.create_settings_if_not_exists()
