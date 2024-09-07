from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.abandoned.models import AbandonedObject


@admin.register(AbandonedObject)
class AbandonedObjectAdmin(TranslationAdmin):
    list_display = ("name", "area", "created_at")
    readonly_fields = ("created_at",)
