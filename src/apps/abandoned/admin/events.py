from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.abandoned.models import Event
from src.apps.dashboard.admin.site import site


@admin.register(Event, site=site)
class EventAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("name",)
    readonly_fields = ("created_at",)
