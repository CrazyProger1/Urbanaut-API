from simple_history.admin import SimpleHistoryAdmin
from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.abandoned.models import AbandonedArea
from src.apps.dashboard.admin.site import site


@admin.register(AbandonedArea, site=site)
class AbandonedAreaAdmin(ModelAdmin, TabbedTranslationAdmin, SimpleHistoryAdmin):
    list_display = (
        "id",
        "name",
        "area",
    )
    list_display_links = ("name",)
