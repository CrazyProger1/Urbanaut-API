from unfold.admin import ModelAdmin
from django.contrib import admin

from src.apps.actions.models import Action
from src.apps.dashboard.admin import site


@admin.register(Action, site=site)
class ActionAdmin(ModelAdmin):
    list_display = ("id", "type", "user")
    search_fields = ("type",)
    list_filter = ("type",)
    list_display_links = ("type",)
