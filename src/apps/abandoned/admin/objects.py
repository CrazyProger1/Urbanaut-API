from unfold.admin import ModelAdmin, TabularInline
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.abandoned.models import AbandonedObject, AbandonedObjectFile
from src.apps.dashboard.admin.site import site


class AbandonedObjectFileInline(TabularInline):
    model = AbandonedObjectFile
    extra = 0


@admin.register(AbandonedObject, site=site)
class AbandonedObjectAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = (AbandonedObjectFileInline,)
    list_display = (
        "id",
        "name",
        "created_at",
    )
    readonly_fields = ("created_at",)
    list_display_links = ("name",)

    search_fields = ("id", "name")
    raw_id_fields = (
        "creator",
        "category",
        "area",
    )
