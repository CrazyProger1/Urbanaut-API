from simple_history.admin import SimpleHistoryAdmin
from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.accounts.models import Rank
from src.apps.dashboard.admin.site import site


@admin.register(Rank, site=site)
class RankAdmin(ModelAdmin, TabbedTranslationAdmin, SimpleHistoryAdmin):
    list_display = (
        "id",
        "name",
        "key",
    )
    list_display_links = (
        "name",
    )
