from rest_framework import routers

from src.apps.media.views.files import FileViewSet

router = routers.SimpleRouter()

router.register("api/v1/media", FileViewSet, basename="file")

urlpatterns = [*router.urls]
