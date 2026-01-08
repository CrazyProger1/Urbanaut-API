from rest_framework import routers

from src.apps.abandoned.views import PlaceViewSet
from src.apps.abandoned.views import AreaViewSet

router = routers.DefaultRouter()

router.register("api/v1/places", PlaceViewSet)
router.register("api/v1/areas", AreaViewSet)

urlpatterns = [*router.urls]
