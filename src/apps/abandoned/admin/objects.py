from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.abandoned.models import AbandonedObject


@admin.register(AbandonedObject)
class AbandonedObjectAdmin(TranslationAdmin):
    list_display = ("name", "area",)
