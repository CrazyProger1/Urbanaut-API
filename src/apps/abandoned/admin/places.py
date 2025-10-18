from django import forms
from django.contrib import admin
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin
from rest_framework.reverse import reverse
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

from src.apps.abandoned.admin.security import PlaceSecurityInline
from src.apps.abandoned.models import Place
from src.apps.accounts.sites import site
from src.utils.django.admin import CreatedByAdminMixin


class ManualPointWidget(forms.MultiWidget):
    template_name = 'django/forms/widgets/multiwidget.html'  # Uses Django's default multi-widget template

    def __init__(self, attrs=None):
        # Child widgets: lat (y) first, then lon (x) for intuitive order
        children = [
            forms.NumberInput(
                attrs={
                    'placeholder': 'Latitude (e.g., 40.7128)',
                    'step': 'any',
                    'min': '-90',
                    'max': '90',
                    'class': 'form-control rounded border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500',  # Tailwind for Unfold
                }
            ),
            forms.NumberInput(
                attrs={
                    'placeholder': 'Longitude (e.g., -74.0060)',
                    'step': 'any',
                    'min': '-180',
                    'max': '180',
                    'class': 'form-control rounded border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500',  # Tailwind
                }
            ),
        ]
        # Wrapper attrs for the whole widget (Unfold-friendly)
        wrapper_attrs = {
            'class': 'grid grid-cols-2 gap-4 mb-4',  # Side-by-side layout
        }
        if attrs:
            wrapper_attrs.update(attrs)
        super().__init__(children, attrs=wrapper_attrs)

    def decompress(self, value):
        """Split Point into [lat, lon] for rendering."""
        if isinstance(value, Point):
            return [value.y, value.x]  # GeoDjango: y=lat, x=lon
        if value:
            try:
                p = Point(value)
                return [p.y, p.x]
            except:
                pass
        return [None, None]

    def value_from_datadict(self, data, files, name):
        """Combine lat/lon inputs into a Point."""
        lat, lon = super().value_from_datadict(data, files, name)
        if lat is not None and lon is not None:
            try:
                # Validate ranges
                lat_f = float(lat)
                lon_f = float(lon)
                if -90 <= lat_f <= 90 and -180 <= lon_f <= 180:
                    return Point(lon_f, lat_f)  # Point(x=lon, y=lat)
            except (ValueError, TypeError):
                pass
        return None

    def format_output(self, rendered_widgets):
        """Wrap with labels for clarity (optional, but UX-friendly)."""
        lat_html, lon_html = rendered_widgets
        return forms.utils.format_html(
            '<label class="block text-sm font-medium text-gray-700 mb-1">Latitude</label>{}<br>'
            '<label class="block text-sm font-medium text-gray-700 mb-1">Longitude</label>{}',
            lat_html, lon_html
        )

@admin.register(Place, site=site)
class PlaceAdmin(CreatedByAdminMixin, TabbedTranslationAdmin, ModelAdmin):
    inlines = (PlaceSecurityInline,)
    created_by_field = "created_by"
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        models.PointField: {
            "widget": ManualPointWidget,
        },
    }
    list_display = (
        "name",
        created_by_field,
        "display_area",
        "created_at",
    )
    autocomplete_fields = (
        created_by_field,
        "area",
    )
    search_fields = (
        "name",
        "description",
        "area__name",
    )
    list_filter = (
        "security__level",
        "created_at",
        "built_at",
        "abandoned_at",
        "area",
    )
    list_per_page = 50

    def display_area(self, obj: Place):
        if obj.area_id:
            area_link = reverse("admin:abandoned_place_changelist")
            return mark_safe(
                f"<a class='underline text-blue-500' href='{area_link}?area__id__exact={obj.area_id}'>{str(obj.area)}</a>"
            )
        return None

    display_area.short_description = _("area")
