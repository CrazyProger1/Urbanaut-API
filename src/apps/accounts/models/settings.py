import logging

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.enums import UITheme

logger = logging.getLogger(__name__)


class Settings(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="settings",
        verbose_name=_("user"),
        primary_key=True,
    )
    language = models.CharField(
        max_length=10,
        choices=settings.LANGUAGES,
        default="en",
        verbose_name=_("language"),
        help_text=_("Preferred language of the user."),
    )
    is_notifications_enabled = models.BooleanField(
        default=True,
        null=False,
        blank=False,
        verbose_name=_("notifications"),
        help_text=_("Notifications enabled."),
    )
    theme = models.CharField(
        max_length=10,
        choices=UITheme,
        default=UITheme.DARK,
        verbose_name=_("theme"),
        help_text=_("Preferred theme of the user."),
    )

    def __str__(self):
        return str(self.user)


class SettingsMixin(models.Model):
    def _update_settings(self):
        if not self.pk or not hasattr(self, "settings"):
            Settings.objects.create(user=self)
            logger.info("Created settings instance for new user")

    def save(self, *args, **kwargs):
        super().save(
            *args,
            **kwargs,
        )
        self._update_settings()

    class Meta:
        abstract = True
