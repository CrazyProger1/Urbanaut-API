from unfold.admin import TabularInline
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.models import Settings


class SettingsInline(TabularInline):
    model = Settings
    can_delete = False
    verbose_name_plural = _("Settings")
    verbose_name = _("Settings")
    tab = True
