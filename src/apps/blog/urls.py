from rest_framework import routers

from src.apps.blog.views import BlogPostViewSet

router = routers.SimpleRouter()

router.register("api/v1/posts", BlogPostViewSet)

urlpatterns = [*router.urls]
