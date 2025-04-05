from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.enums import UITheme
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
    is_animations_enabled = models.BooleanField(
        default=True,
        null=False,
        blank=False,
        verbose_name=_("animations"),
        help_text=_("Enable animations."),
    )
    is_newsletters_enabled = models.BooleanField(
        default=True,
        null=False,
        blank=False,
        verbose_name=_("newsletters"),
        help_text=_("Enable newsletters."),
    )
    is_notifications_enabled = models.BooleanField(
        default=True,
        null=False,
        blank=False,
        verbose_name=_("notifier"),
        help_text=_("Enable notifier."),
    )
    theme = models.CharField(
        max_length=10,
        choices=UITheme,
        default=UITheme.DARK,
        verbose_name=_("theme"),
        help_text=_("Preferred theme of the user."),
    )

    def __str__(self):
        return "Settings"


class SettingsUserModelMixin(models.Model):
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
