from simple_history.admin import SimpleHistoryAdmin
from unfold.admin import ModelAdmin, TabularInline
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.decorators import display

from src.apps.abandoned.models import (
    AbandonedObject,
    AbandonedObjectFile,
    AbandonedObjectCategory,
)
from src.apps.dashboard.admin.site import site


class AbandonedObjectTabularFileInline(TabularInline):
    model = AbandonedObjectFile
    extra = 0
    show_change_link = True
    tab = True
    verbose_name = _("File")
    verbose_name_plural = _("Files")


class AbandonedObjectCategoryTabularInline(TabularInline):
    model = AbandonedObjectCategory
    extra = 0
    raw_id_fields = ("category",)
    show_change_link = True
    tab = True
    verbose_name = _("Category")
    verbose_name_plural = _("Categories")


@admin.register(AbandonedObject, site=site)
class AbandonedObjectAdmin(SimpleHistoryAdmin, ModelAdmin, TabbedTranslationAdmin):
    inlines = (
        AbandonedObjectTabularFileInline,
        AbandonedObjectCategoryTabularInline,
    )
    exclude = (
        "viewable",
    )
    list_display = (
        "id",
        "name",
        "rating",
        "views",
        "created_at",

    )
    readonly_fields = (
        "created_at",
        "rating",
        "views",
    )
    list_display_links = ("name",)

    search_fields = ("id", "name")
    raw_id_fields = (
        "created_by",
        "area",
    )
