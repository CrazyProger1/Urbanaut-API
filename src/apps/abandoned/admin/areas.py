from django.contrib import admin
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin, StackedInline
from unfold.contrib.forms.widgets import WysiwygWidget

from src.apps.abandoned.models import Area, AreaTag
from src.apps.accounts.sites import site
from src.utils.django.admin import CreatedByAdminMixin
from src.utils.django.geo import ManualGeometryFieldWidget


class AreaTagInline(StackedInline):
    tab = True
    model = AreaTag
    extra = 1
    verbose_name = _("Tag")
    verbose_name_plural = _("Tags")


@admin.register(Area, site=site)
class AreaAdmin(CreatedByAdminMixin, TabbedTranslationAdmin, ModelAdmin):
    inlines = (AreaTagInline,)
    created_by_field = "created_by"
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        models.PolygonField: {
            "widget": ManualGeometryFieldWidget,
        },
    }
    list_display = (
        "name",
        created_by_field,
        "created_at",
        "is_private",
    )
    autocomplete_fields = (created_by_field,)
    search_fields = (
        "name",
        "description",
    )
    list_filter = ("created_at",)
