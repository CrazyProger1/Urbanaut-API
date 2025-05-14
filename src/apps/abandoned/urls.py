from rest_framework import routers

from src.apps.abandoned.views import (
    AbandonedObjectViewSet,
    AbandonedAreaViewSet,
    AbandonedObjectCategoryViewSet, EventViewSet,
)

router = routers.SimpleRouter()

router.register("api/v1/objects", AbandonedObjectViewSet, basename="objects")
router.register("api/v1/areas", AbandonedAreaViewSet, basename="areas")
router.register("api/v1/categories", AbandonedObjectCategoryViewSet, basename="categories")
router.register("api/v1/events", EventViewSet, basename="events")

urlpatterns = [*router.urls]
