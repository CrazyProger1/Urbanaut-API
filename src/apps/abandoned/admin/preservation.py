from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin, StackedInline

from src.apps.abandoned.models import PlacePreservation
from src.apps.accounts.sites import site


@admin.register(PlacePreservation, site=site)
class PlacePreservationAdmin(ModelAdmin):
    pass


class PlacePreservationInline(StackedInline):
    model = PlacePreservation
    extra = 0
    can_delete = False
    verbose_name = _("Preservation")
    verbose_name_plural = _("Preservation")
