from django.contrib import admin
from unfold.admin import ModelAdmin

from src.apps.abandoned.models import Provider
from src.apps.accounts.sites import site


@admin.register(Provider, site=site)
class ProviderAdmin(ModelAdmin):
    list_display = ("name", "created_at",)
