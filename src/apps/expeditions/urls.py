from rest_framework.routers import DefaultRouter

from src.apps.expeditions.views import ExpeditionViewSet, ReportViewSet

router = DefaultRouter()

router.register(r"api/v1/reports", ReportViewSet)
router.register(r"api/v1/expeditions", ExpeditionViewSet)

urlpatterns = router.urls
