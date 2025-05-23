from django.urls import path
from rest_framework import routers

from src.apps.accounts.views import (
    UserViewSet,
    TeamViewSet,
    get_languages,
    ReferralLinkViewSet,
    SettingsAPIView,
    TermsViewSet, FriendViewSet,
)
from src.apps.accounts.views.referrals import ReferralViewSet

router = routers.SimpleRouter()

router.register("api/v1/users", UserViewSet, basename="users")
router.register("api/v1/teams", TeamViewSet, basename="teams")
router.register("api/v1/referral_links", ReferralLinkViewSet, basename="referral_links")
router.register("api/v1/referrals", ReferralViewSet, basename="referrals")
router.register("api/v1/terms", TermsViewSet, basename="terms")
router.register("api/v1/friends", FriendViewSet, basename="friends")

urlpatterns = [
    path("api/v1/languages", get_languages),
    path("api/v1/settings/", SettingsAPIView.as_view(), name="settings"),
]

urlpatterns += router.urls
