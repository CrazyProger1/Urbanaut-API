from django.urls import path, include

urlpatterns = [
    path("", include("src.apps.dashboard.urls")),
    path("", include("src.apps.abandoned.urls")),
    path("", include("src.apps.accounts.urls")),
    path("", include("src.apps.notifications.urls")),
    path("", include("src.apps.actions.urls")),
    path("", include("src.apps.docs.urls")),
    path("", include("src.apps.media.urls")),
    path("", include("src.apps.blog.urls")),
    path("", include("src.apps.ratings.urls")),
    path("mdeditor/", include('mdeditor.urls'))
]
