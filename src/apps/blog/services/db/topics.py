from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from src.apps.blog.models import BlogTopic

User = get_user_model()


def get_available_blog_topics(user: User = None) -> QuerySet[BlogTopic]:
    return BlogTopic.objects.visible(user=user)
