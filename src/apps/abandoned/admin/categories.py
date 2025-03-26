from typing import Any

from django.db.models import Model
from django.forms import Form
from django.http import HttpRequest
from simple_history.admin import SimpleHistoryAdmin
from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.abandoned.models import Category
from src.apps.dashboard.admin.site import site


@admin.register(Category, site=site)
class CategoryAdmin(ModelAdmin, TabbedTranslationAdmin, SimpleHistoryAdmin):
    list_display = (
        "id",
        "name",
        "created_by",
    )
    list_display_links = ("name",)
    raw_id_fields = (
        "created_by",
        "parent",
    )
    list_filter = (
        "created_at",
    )
    search_fields = (
        "name",
        "description",
    )

    def save_model(
            self,
            request: HttpRequest,
            obj: Category,
            form: Form,
            change: Any,
    ) -> None:
        if not obj.created_by:
            obj.created_by = request.user
        return super().save_model(request, obj, form, change)
