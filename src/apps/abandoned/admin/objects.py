from simple_history.admin import SimpleHistoryAdmin
from unfold.admin import ModelAdmin, TabularInline
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.abandoned.models import AbandonedObject, AbandonedObjectFile, AbandonedObjectCategory
from src.apps.dashboard.admin.site import site


class AbandonedObjectTabularFileInline(TabularInline):
    model = AbandonedObjectFile
    extra = 0
    show_change_link = True
    tab = True


class AbandonedObjectCategoryTabularInline(TabularInline):
    model = AbandonedObjectCategory
    extra = 0
    raw_id_fields = (
        "category",
    )
    show_change_link = True
    tab = True


@admin.register(AbandonedObject, site=site)
class AbandonedObjectAdmin(SimpleHistoryAdmin, ModelAdmin, TabbedTranslationAdmin):
    inlines = (
        AbandonedObjectTabularFileInline,
        AbandonedObjectCategoryTabularInline,
    )
    list_display = (
        "id",
        "name",
        "created_at",
    )
    readonly_fields = ("created_at",)
    list_display_links = ("name",)

    search_fields = ("id", "name")
    raw_id_fields = (
        "created_by",
        "area",
    )
