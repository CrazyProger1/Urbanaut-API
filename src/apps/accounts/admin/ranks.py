from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.accounts.models import Rank
from src.apps.dashboard.admin.site import site


@admin.register(Rank, site=site)
class RankAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = (
        "name",
    )
