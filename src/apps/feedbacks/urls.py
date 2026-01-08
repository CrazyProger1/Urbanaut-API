from rest_framework import routers

from src.apps.feedbacks.views import FeedbackViewSet

router = routers.DefaultRouter()

router.register("api/v1/feedbacks", FeedbackViewSet)
urlpatterns = [
    *router.urls,
]
