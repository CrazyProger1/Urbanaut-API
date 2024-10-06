from rest_framework import routers

from src.apps.blog.views import BlogPostViewSet, BlogTopicViewSet

router = routers.SimpleRouter()

router.register("api/v1/posts", BlogPostViewSet)
router.register("api/v1/topics", BlogTopicViewSet)

urlpatterns = [*router.urls]
