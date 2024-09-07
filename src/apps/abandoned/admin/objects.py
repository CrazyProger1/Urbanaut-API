from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.abandoned.models import AbandonedObject


@admin.register(AbandonedObject)
class AbandonedObjectAdmin(TranslationAdmin):
    list_display = ("id", "name", "area", "created_at")
    readonly_fields = ("created_at",)
    list_display_links = ("name",)

    search_fields = ("id", "name")
