from rest_framework import routers

from src.apps.media.views import FileViewSet

router = routers.DefaultRouter()
router.register("api/v1/files", FileViewSet, basename="file")

urlpatterns = [
    *router.urls,
]
