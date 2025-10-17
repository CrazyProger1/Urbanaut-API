from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin
from rest_framework.reverse import reverse
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

from src.apps.abandoned.models import Place
from src.apps.accounts.sites import site
from src.utils.django.admin import CreatedByAdminMixin


@admin.register(Place, site=site)
class PlaceAdmin(CreatedByAdminMixin, TabbedTranslationAdmin, ModelAdmin):
    created_by_field = "created_by"
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
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
