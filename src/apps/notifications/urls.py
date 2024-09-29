from rest_framework import routers

from src.apps.notifications.views import NotificationViewSet

router = routers.SimpleRouter()

router.register("api/v1/notifications", NotificationViewSet)

urlpatterns = [*router.urls]
