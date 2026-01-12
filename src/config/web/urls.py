from django.urls import path, include

urlpatterns = [
    path("", include("src.apps.accounts.urls")),
    path("", include("src.apps.docs.urls")),
    path("", include("src.apps.abandoned.urls")),
    path("", include("src.apps.tags.urls")),
    path("", include("src.apps.feedbacks.urls")),
    path("", include("src.apps.geo.urls")),
    path("", include("src.apps.media.urls")),
]
