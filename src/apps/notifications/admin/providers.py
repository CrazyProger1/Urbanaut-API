from django.contrib import admin
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.notifications.models import NotificationProvider


@admin.register(NotificationProvider, site=site)
class ProviderAdmin(ModelAdmin):
    list_display = ("name", "is_enabled")
    list_filter = ("is_enabled",)
    search_fields = ("name",)
