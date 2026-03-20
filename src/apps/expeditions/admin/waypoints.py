from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.sites import site
from src.apps.expeditions.models import Waypoint


class WaypointInline(StackedInline):
    model = Waypoint
    extra = 1
    tab = True
    verbose_name = _("Waypoint")
    verbose_name_plural = _("Waypoints")
    autocomplete_fields = ("place",)


@admin.register(Waypoint, site=site)
class WaypointAdmin(ModelAdmin):
    pass
