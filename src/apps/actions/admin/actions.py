from unfold.admin import ModelAdmin
from django.contrib import admin

from src.apps.actions.models import Action


@admin.register(Action)
class ActionAdmin(ModelAdmin):
    list_display = ("id", "type", "user")
    search_fields = ("type",)
    list_filter = ("type",)
    list_display_links = ("type",)
