from rest_framework import routers

from src.apps.notifier.views import NotificationViewSet

router = routers.SimpleRouter()

router.register("api/v1/notifier", NotificationViewSet)

urlpatterns = [*router.urls]
