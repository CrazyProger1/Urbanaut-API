from django.contrib import admin
from django.contrib.gis.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin
from rest_framework.reverse import reverse
from unfold.admin import ModelAdmin, StackedInline
from unfold.contrib.forms.widgets import WysiwygWidget

from src.apps.abandoned.admin.security import PlaceSecurityInline
from src.apps.abandoned.admin.preservation import PlacePreservationInline
from src.apps.abandoned.models import Place, PlaceTag
from src.apps.accounts.sites import site
from src.utils.django.admin import CreatedByAdminMixin
from src.utils.django.geo import ManualGeometryFieldWidget


class PlaceTagInline(StackedInline):
    tab = True
    model = PlaceTag
    extra = 1
    verbose_name = _("Tag")
    verbose_name_plural = _("Tags")


@admin.register(Place, site=site)
class PlaceAdmin(CreatedByAdminMixin, TabbedTranslationAdmin, ModelAdmin):
    inlines = (
        PlaceSecurityInline,
        PlacePreservationInline,
        PlaceTagInline,
    )
    created_by_field = "created_by"
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        models.PointField: {
            "widget": ManualGeometryFieldWidget,
        },
    }
    list_display = (
        "name",
        created_by_field,
        "display_area",
        "created_at",
        "is_private",
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
