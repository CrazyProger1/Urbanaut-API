from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin, StackedInline

from src.apps.abandoned.models import PlaceSecurity
from src.apps.accounts.sites import site


@admin.register(PlaceSecurity, site=site)
class PlaceSecurityAdmin(ModelAdmin):
    pass


class PlaceSecurityInline(StackedInline):
    model = PlaceSecurity
    extra = 0
    can_delete = False
    verbose_name = _("Security")
    verbose_name_plural = _("Security")
