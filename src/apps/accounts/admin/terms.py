from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.accounts.models import Terms
from src.apps.dashboard.admin.site import site


@admin.register(Terms, site=site)
class TermsAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "version",
        "is_active",
    )
    list_display_links = (
        "version",
    )
    list_filter = (
        "is_active",
        "version",
    )
    search_fields = (
        "version",
    )
