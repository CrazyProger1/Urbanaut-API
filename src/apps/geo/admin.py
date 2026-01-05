from cities_light.admin import (
    CountryAdmin as LightCountryAdmin,
    CityAdmin as LightCityAdmin,
    RegionAdmin as LightRegionAdmin,
    SubRegionAdmin as LightSubRegionAdmin,
)
from django.contrib import admin
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.geo.models import Country, Region, City, SubRegion


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
    pass
