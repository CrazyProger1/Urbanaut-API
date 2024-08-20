from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.abandoned.models import Event


@admin.register(Event)
class EventAdmin(TranslationAdmin):
    list_display = ("name",)
