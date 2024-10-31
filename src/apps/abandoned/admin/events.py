from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.abandoned.models import Event


@admin.register(Event)
class EventAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("name",)
    readonly_fields = ("created_at",)
