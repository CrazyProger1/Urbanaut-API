from django.contrib import admin
from django.db import models
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

from src.apps.abandoned.models import Area
from src.apps.accounts.sites import site
from src.utils.django.admin import CreatedByAdminMixin


@admin.register(Area, site=site)
class AreaAdmin(CreatedByAdminMixin, TabbedTranslationAdmin, ModelAdmin):
    created_by_field = "created_by"
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    list_display = (
        "name",
        created_by_field,
        "created_at",
    )
    autocomplete_fields = (created_by_field,)
    search_fields = (
        "name",
        "description",
    )
    list_filter = ("created_at",)
