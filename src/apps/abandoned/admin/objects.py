from django.db import models
from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

from src.apps.abandoned.models import AbandonedObject


@admin.register(AbandonedObject)
class AbandonedObjectAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "name", "area", "created_at")
    readonly_fields = ("created_at",)
    list_display_links = ("name",)

    search_fields = ("id", "name")
