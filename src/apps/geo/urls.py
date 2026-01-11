from rest_framework import routers

from src.apps.geo.views import CountryViewSet, CityViewSet

router = routers.DefaultRouter()

router.register("api/v1/countries", CountryViewSet)
router.register("api/v1/cities", CityViewSet)

urlpatterns = [
    *router.urls,
]
