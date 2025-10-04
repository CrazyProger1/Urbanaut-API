from django.urls import path
from djoser.views import TokenCreateView, TokenDestroyView, UserViewSet

from src.apps.accounts.sites import site
from src.apps.accounts.views import (
    GoogleOauthRedirectURIView,
    GoogleOauthCallbackView,
)

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
    path("api/v1/tokens/", TokenCreateView.as_view(), name="jwt-create"),
    path("api/v1/tokens/", TokenDestroyView.as_view(), name="jwt-destroy"),
    path("api/v1/users/", UserViewSet.as_view({"post": "create"}), name="user-register"),
    path("api/v1/users/<int:pk>/", UserViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }), name="user-detail"),

    path("api/v1/users/me/", UserViewSet.as_view({
        "get": "me",
        "put": "me",
        "patch": "me",
        "delete": "me"
    }), name="user-me"),

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
