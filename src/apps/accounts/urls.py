from rest_framework import routers

from src.apps.accounts.views import UserViewSet

router = routers.SimpleRouter()

router.register("api/v1/users", UserViewSet)

urlpatterns = [*router.urls]
