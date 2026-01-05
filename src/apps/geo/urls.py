from rest_framework import routers

from src.apps.geo.views import CountryViewSet

router = routers.DefaultRouter()

router.register("api/v1/countries", CountryViewSet)

urlpatterns = [
    *router.urls,
]
