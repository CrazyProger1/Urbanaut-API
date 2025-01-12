from django.urls import path

from src.apps.dashboard.admin import site

urlpatterns = [
    path("admin/", site.urls),
]
