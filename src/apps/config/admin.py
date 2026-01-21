import logging
import os

from constance.forms import ConstanceForm
from django.contrib import admin
from constance.admin import Config, ConstanceAdmin

from src.apps.accounts.sites import site

logger = logging.getLogger(__name__)


class ConstanceConfigAdminForm(ConstanceForm):
    def save(self):
        super().save()
        maintenance = self.cleaned_data["MAINTENANCE"]
        try:
            if maintenance:
                open("/var/www/maintenance_on.flag")
                logger.info("Maintenance mode enabled")
            else:
                os.remove("/var/www/maintenance_on.flag")
                logger.info("Maintenance mode disabled")
        except FileNotFoundError:
            logger.warning("Maintenance flag not found")
        except Exception as e:
            logger.error(f"An error occurred while switching maintenance: {e}", exc_info=e)


@admin.register(Config, site=site)
class ConstanceConfigAdmin(ConstanceAdmin):
    change_list_form = ConstanceConfigAdminForm
