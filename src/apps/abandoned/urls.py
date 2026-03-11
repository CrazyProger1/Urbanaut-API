from django.urls import path
from rest_framework import routers

from src.apps.abandoned.views import PlaceViewSet, GeoJSONMapAPIView, AreaViewSet

router = routers.DefaultRouter()

router.register("api/v1/places", PlaceViewSet)
router.register("api/v1/areas", AreaViewSet)

urlpatterns = [
    path("api/v1/map/", GeoJSONMapAPIView.as_view()),
    *router.urls,
]
