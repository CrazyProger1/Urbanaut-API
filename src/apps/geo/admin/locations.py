from django.contrib import admin

from src.apps.geo.models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass