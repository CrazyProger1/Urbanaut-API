from django.urls import path

from src.apps.stats.views import GlobalStatsView

urlpatterns = [
    path("api/v1/stats/", GlobalStatsView.as_view()),
]
