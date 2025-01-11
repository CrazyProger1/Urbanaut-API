from typing import Any

from django.db.models import Model
from django.forms import Form
from django.http import HttpRequest
from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.abandoned.models import AbandonedObjectCategory


@admin.register(AbandonedObjectCategory)
class AbandonedObjectCategoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "name",
        "creator",
    )
    list_display_links = ("name",)
    raw_id_fields = (
        "creator",
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
            obj: Model,
            form: Form,
            change: Any,
    ) -> None:
        if not obj.creator:
            obj.creator = request.user
        return super().save_model(request, obj, form, change)