from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.abandoned.models import AbandonedArea


@admin.register(AbandonedArea)
class AbandonedAreaAdmin(TranslationAdmin):
    list_display = (
        "id",
        "name",
        "area",
    )
    list_display_links = ("name",)
