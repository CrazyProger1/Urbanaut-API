from django.urls import path
from rest_framework import routers

from src.apps.accounts.views import (
    UserViewSet,
    TeamViewSet,
    get_languages,
    ReferralLinkViewSet,
    SettingsAPIView,
)

router = routers.SimpleRouter()

router.register("api/v1/users", UserViewSet)
router.register("api/v1/teams", TeamViewSet)
router.register("api/v1/referral_links", ReferralLinkViewSet)

urlpatterns = [
    path("api/v1/languages", get_languages),
    path("api/v1/settings/", SettingsAPIView.as_view(), name="settings"),
]

urlpatterns += router.urls
