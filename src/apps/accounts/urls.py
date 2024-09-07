from rest_framework import routers

from src.apps.accounts.views import UserViewSet, TeamViewSet, NotificationViewSet

router = routers.SimpleRouter()

router.register("api/v1/users", UserViewSet)
router.register("api/v1/teams", TeamViewSet)
router.register("api/v1/notifications", NotificationViewSet)

urlpatterns = [*router.urls]
