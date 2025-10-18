from django.contrib import admin
from django.contrib.gis.db import models
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

from src.apps.abandoned.models import Area
from src.apps.accounts.sites import site
from src.utils.django.admin import CreatedByAdminMixin

from django import forms
from django.contrib.gis.geos import Polygon
from django.utils.safestring import mark_safe


class ManualPolygonWidget(forms.Textarea):
    def __init__(self, attrs=None):
        default_attrs = {
            'rows': 6,
            'placeholder': 'POLYGON((lon1 lat1, lon2 lat2, lon3 lat3, lon1 lat1))  # Close the ring; add MULTIPOLYGON(...) for multiples',
            'class': 'form-control rounded-lg border border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 resize-vertical',
            # Tailwind + resizable
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

    def value_from_datadict(self, data, files, name):
        """Parse WKT input to Polygon."""
        wkt = data.get(name)
        if wkt and wkt.strip():
            try:
                # Assume EWKT (with optional SRID=4326 prefix); strip whitespace
                geom = Polygon.from_ewkt(wkt.strip())
                if geom.geom_type == 'Polygon':  # Validate it's a Polygon (not Point/Line)
                    return geom
            except Exception:
                pass  # Silently fail; form errors will show on save
        return None

    def format_output(self, rendered_widget):
        """Add styled label and example for UX."""
        example = """
POLYGON((-74.006 40.712, -73.935 40.712, -73.935 40.758, -74.006 40.758, -74.006 40.712))
# Notes:
# - List lon lat pairs clockwise/counter-clockwise, closing the ring (last = first).
# - For holes: POLYGON((exterior...), (interior1...)).
# - For multiple polygons: MULTIPOLYGON(((...)), ((...))).
# - Use decimal degrees (lon: -180 to 180, lat: -90 to 90).
        """
        return mark_safe(
            f'''
            <label class="block text-sm font-medium text-gray-700 mb-1">Polygon Geometry (WKT Format)</label>
            <div class="text-xs text-gray-500 mb-2 p-2 bg-gray-50 rounded border border-gray-200">
                <strong>Example:</strong><br>{example}
            </div>
            {rendered_widget}
            '''
        )


@admin.register(Area, site=site)
class AreaAdmin(CreatedByAdminMixin, TabbedTranslationAdmin, ModelAdmin):
    created_by_field = "created_by"
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        models.PolygonField: {
            "widget": ManualPolygonWidget,
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
