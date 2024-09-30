from django.urls import path
from rest_framework import routers

from src.apps.accounts.views import UserViewSet, TeamViewSet, get_languages

router = routers.SimpleRouter()

router.register("api/v1/users", UserViewSet)
router.register("api/v1/teams", TeamViewSet)

urlpatterns = [
    path("api/v1/languages", get_languages),
]

urlpatterns += router.urls
