from rest_framework import routers

from src.apps.feedbacks.views import FeedbackViewSet, RequestViewSet

router = routers.DefaultRouter()

router.register("api/v1/feedbacks", FeedbackViewSet)
router.register("api/v1/requests", RequestViewSet)

urlpatterns = [
    *router.urls,
]
