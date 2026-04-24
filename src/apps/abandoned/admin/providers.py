from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from src.apps.abandoned.models import Provider
from src.apps.accounts.sites import site
from src.utils.django.admin import CreatedByAdminMixin


@admin.register(Provider, site=site)
class ProviderAdmin(ModelAdmin, TabbedTranslationAdmin, CreatedByAdminMixin):
    created_by_field = "created_by"
    list_display = (
        "name",
        "created_at",
        created_by_field,
    )
    search_fields = ("name",)
    autocomplete_fields = (created_by_field,)

    def get_changeform_initial_data(self, request):
        return {"created_by": request.user}
