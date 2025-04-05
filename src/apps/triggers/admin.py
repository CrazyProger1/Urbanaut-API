from unfold.admin import ModelAdmin
from django.contrib import admin

from src.apps.dashboard.admin import site
from src.apps.triggers.models import Trigger


@admin.register(Trigger, site=site)
class TriggerAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_triggered",
        "triggered_at",
    )
    list_display_links = (
        "name",
    )
