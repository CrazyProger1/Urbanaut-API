from rest_framework import routers

from src.apps.abandoned.views import (
    AbandonedObjectViewSet,
    AbandonedAreaViewSet,
    AbandonedObjectCategoryViewSet,
)

router = routers.SimpleRouter()

router.register("api/v1/objects", AbandonedObjectViewSet)
router.register("api/v1/areas", AbandonedAreaViewSet)
router.register("api/v1/categories", AbandonedObjectCategoryViewSet)

urlpatterns = [*router.urls]
