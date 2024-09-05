from rest_framework import routers

from src.apps.abandoned.views import ObjectViewSet, AreaViewSet

router = routers.SimpleRouter()

router.register("objects", ObjectViewSet)
router.register("areas", AreaViewSet)

urlpatterns = [*router.urls]
