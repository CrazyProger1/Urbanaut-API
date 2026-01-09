from cities_light.admin import (
    CountryAdmin as LightCountryAdmin,
    CityAdmin as LightCityAdmin,
    RegionAdmin as LightRegionAdmin,
    SubRegionAdmin as LightSubRegionAdmin,
)
from django.contrib import admin
from django.contrib.gis.db import models
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.geo.models import Country, Region, City, SubRegion, Address
from src.utils.django.geo import ManualGeometryFieldWidget


@admin.register(Country, site=site)
class CountryAdmin(ModelAdmin, LightCountryAdmin):
    list_display = (
        "name",
        "code2",
        "code3",
        "continent",
        "tld",
        "phone",
        "geoname_id",
        "is_active",
    )


@admin.register(Region, site=site)
class RegionAdmin(ModelAdmin, LightRegionAdmin):
    pass


@admin.register(SubRegion, site=site)
class SubRegionAdmin(ModelAdmin, LightSubRegionAdmin):
    pass


@admin.register(City, site=site)
class CityAdmin(ModelAdmin, LightCityAdmin):
    formfield_overrides = {
        models.PointField: {
            "widget": ManualGeometryFieldWidget,
        },
    }


@admin.register(Address, site=site)
class AddressAdmin(ModelAdmin):
    list_display = ("text",)
    autocomplete_fields = (
        "country",
        "region",
        "subregion",
        "city",
    )
    search_fields = ("text",)
