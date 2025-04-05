from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.db import create_object


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


class SettingsUserMixin(models.Model):
    class Meta:
        abstract = True

    def create_settings_if_not_exists(self):
        if not self.settings:
            self.settings = create_object(source=Settings)
            self.save(update_fields=["settings"])

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
