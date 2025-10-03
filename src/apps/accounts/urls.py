from django.urls import path

from src.apps.accounts.sites import site
from src.apps.accounts.views import GoogleOauthRedirectURIView, GoogleOauthCallbackView

urlpatterns = [
    path("admin/", site.urls),
    path("api/v1/google/oauth/uri", GoogleOauthRedirectURIView.as_view(), name="google-oauth-redirect-uri"),
    path("api/v1/google/oauth/callback", GoogleOauthCallbackView.as_view(), name="google-oauth-callback")
]
