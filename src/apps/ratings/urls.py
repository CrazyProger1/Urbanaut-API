from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from src.apps.ratings.views import RatingViewSet, RatingVoteViewSet

router = DefaultRouter()
router.register("api/v1/ratings", RatingViewSet, basename="ratings")

ratings_router = NestedSimpleRouter(router, "ratings", lookup="rating")
ratings_router.register("votes", RatingVoteViewSet, basename="rating-votes")

urlpatterns = router.urls + ratings_router.urls
