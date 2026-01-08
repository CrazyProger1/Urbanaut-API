from django.urls import path
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from src.apps.accounts.sites import site
from src.apps.accounts.views import (
    GoogleOauthRedirectURIView,
    GoogleOauthCallbackView,
    SettingsViewSet,
    ReferralCodeViewSet,
    UserViewSet,
)

router = DefaultRouter()

router.register("api/v1/referrals", ReferralCodeViewSet, basename="referrals")
router.register("api/v1/users", UserViewSet, basename="users")

urlpatterns = [
    path("admin/", site.urls),
    path(
        "api/v1/google/oauth/uri/",
        GoogleOauthRedirectURIView.as_view(),
        name="google-oauth-redirect-uri",
    ),
    path(
        "api/v1/google/oauth/callback/",
        GoogleOauthCallbackView.as_view(),
        name="google-oauth-callback",
    ),
    path("api/v1/tokens/", TokenObtainPairView.as_view(), name="jwt-create"),
    path("api/v1/tokens/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),

    path(
        "api/v1/users/me/",
        DjoserUserViewSet.as_view({"get": "me", "put": "me", "patch": "me", "delete": "me"}),
        name="user-me",
    ),
    path(
        "api/v1/settings/",
        SettingsViewSet.as_view(
            {"put": "update", "patch": "partial_update", "get": "retrieve"}
        ),
    ),
    *router.urls,

    # path("api/v1/users/activate/", UserViewSet.as_view({"post": "activation"}), name="user-activate"),
    # path("api/v1/users/resend-activation/", UserViewSet.as_view({"post": "resend_activation"}),
    #      name="user-resend-activation"),
    #
    # path("api/v1/users/set-password/", UserViewSet.as_view({"post": "set_password"}), name="user-set-password"),
    # path("api/v1/users/reset-password/", UserViewSet.as_view({"post": "reset_password"}),
    #      name="user-reset-password"),
    # path("api/v1/users/reset-password-confirm/", UserViewSet.as_view({"post": "reset_password_confirm"}),
    #      name="user-reset-password-confirm"),
    #
    # path("api/v1/users/set-username/", UserViewSet.as_view({"post": "set_username"}), name="user-set-username"),
    # path("api/v1/users/reset-username/", UserViewSet.as_view({"post": "reset_username"}),
    #      name="user-reset-username"),
    # path("api/v1/users/reset-username-confirm/", UserViewSet.as_view({"post": "reset_username_confirm"}),
    #      name="user-reset-username-confirm"),
]
