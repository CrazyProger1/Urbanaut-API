from django.contrib import admin
from django.contrib.gis.db import models
from django.contrib.gis.forms import OSMWidget
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

@admin.register(Place, site=site)
class PlaceAdmin(CreatedByAdminMixin, TabbedTranslationAdmin, ModelAdmin):
    inlines = (PlaceSecurityInline,)
    created_by_field = "created_by"
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        models.PointField: {
            "widget": UnfoldOSMWidget,
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
