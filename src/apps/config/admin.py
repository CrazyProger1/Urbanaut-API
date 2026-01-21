import logging

from constance.forms import ConstanceForm
from django.contrib import admin
from constance.admin import Config, ConstanceAdmin

from src.apps.accounts.sites import site
from src.apps.config.services import switch_maintenance

logger = logging.getLogger(__name__)


class ConstanceConfigAdminForm(ConstanceForm):
    def save(self):
        super().save()

        if "MAINTENANCE" in self.cleaned_data:
            switch_maintenance(maintenance=self.cleaned_data["MAINTENANCE"])


@admin.register(Config, site=site)
class ConstanceConfigAdmin(ConstanceAdmin):
    change_list_form = ConstanceConfigAdminForm
