from rest_framework import routers

from src.apps.news.views import NewsViewSet

router = routers.DefaultRouter()
router.register("api/v1/news", NewsViewSet)

urlpatterns = router.urls
