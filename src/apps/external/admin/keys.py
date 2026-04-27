from django.contrib import admin
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.external.models import Key
from src.utils.django.admin import CreatedByAdminMixin


@admin.register(Key, site=site)
class KeyAdmin(CreatedByAdminMixin, ModelAdmin):
    created_by_field = "created_by"
    list_display = (
        "name",
        created_by_field,
        "created_at",
    )
    autocomplete_fields = (created_by_field, "application",)
    search_fields = (
        "name",
    )
    list_filter = ("created_at",)
