from django.contrib import admin
from django.contrib.gis.forms import OSMWidget
from django.contrib.gis.db import models
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

from src.apps.abandoned.models import Area
from src.apps.accounts.sites import site
from src.utils.django.admin import CreatedByAdminMixin

from django.contrib.gis.forms.widgets import OSMWidget
from django.utils.safestring import mark_safe

class UnfoldOSMWidget(OSMWidget):
    template_name = "gis/unfold_openlayers_osm.html"  # Points to our custom template

    def __init__(self, attrs=None):
        super().__init__(attrs)
        # Enforce base attrs for Unfold compatibility (height, z-index to avoid overlaps)
        default_attrs = {
            'class': 'rounded-lg border border-gray-300 shadow-sm w-full',  # Tailwind classes
            'style': 'height: 400px; z-index: 1000; position: relative;',   # Fix blank sizing/layering
        }
        if attrs:
            default_attrs.update(attrs)
        self.attrs = default_attrs

    def render(self, name, value, attrs=None, renderer=None):
        # Ensure JS initializes after DOM (common blank fix)
        attrs = self.build_attrs(attrs, name=name)
        attrs['data-init-delay'] = 'true'  # Optional: Hook for custom JS if needed
        return super().render(name, value, attrs, renderer)

@admin.register(Area, site=site)
class AreaAdmin(CreatedByAdminMixin, TabbedTranslationAdmin, ModelAdmin):
    created_by_field = "created_by"
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        models.PolygonField: {
            "widget": UnfoldOSMWidget,
        },
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
