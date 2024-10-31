from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.abandoned.models import AbandonedArea


@admin.register(AbandonedArea)
class AbandonedAreaAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "name",
        "area",
    )
    list_display_links = ("name",)
