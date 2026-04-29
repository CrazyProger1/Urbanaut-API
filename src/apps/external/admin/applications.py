from django.contrib import admin
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.external.models import Application
from src.utils.django.admin import CreatedByAdminMixin


@admin.register(Application, site=site)
class ApplicationAdmin(CreatedByAdminMixin, ModelAdmin):
    created_by_field = "created_by"
    list_display = (
        "name",
        created_by_field,
        "created_at",
    )
    autocomplete_fields = (created_by_field,)
    search_fields = ("name",)
    list_filter = ("created_at",)
