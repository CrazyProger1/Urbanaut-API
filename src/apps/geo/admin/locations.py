from unfold.admin import ModelAdmin
from django.contrib import admin

from src.apps.dashboard.admin import site
from src.apps.geo.models import Location


@admin.register(Location, site=site)
class LocationAdmin(ModelAdmin):
    pass
