from rest_framework import routers

from src.apps.abandoned.views import PlaceViewSet

router = routers.DefaultRouter()

router.register("api/v1/places", PlaceViewSet)

urlpatterns = [
    *router.urls
]
