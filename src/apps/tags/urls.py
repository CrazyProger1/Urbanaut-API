from rest_framework.routers import DefaultRouter

from src.apps.tags.views import TagViewSet

router = DefaultRouter()
router.register("api/v1/tags", TagViewSet)

urlpatterns = [*router.urls]
