from django.urls import path
from rest_framework import routers

from src.apps.notifications.consumers import AsyncNotificationConsumer
from src.apps.notifications.views import NotificationViewSet

router = routers.DefaultRouter()
router.register("api/v1/notifications", NotificationViewSet, basename="notifications")

urlpatterns = [
    *router.urls,
]

websocket_urlpatterns = [
    path("ws/notifications/", AsyncNotificationConsumer.as_asgi()),
]
