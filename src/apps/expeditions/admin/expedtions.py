from django.contrib import admin
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.expeditions.models import Expedition
from src.utils.django.admin import CreatedByAdminMixin


@admin.register(Expedition, site=site)
class ExpeditionAdmin(CreatedByAdminMixin, ModelAdmin):
    created_by_field = "created_by"
    list_display = (
        "name",
        "state",
        "created_at",
        created_by_field,
    )
    autocomplete_fields = (created_by_field,)
    search_fields = (
        "name",
        "description",
    )
    list_filter = ("created_at",)
