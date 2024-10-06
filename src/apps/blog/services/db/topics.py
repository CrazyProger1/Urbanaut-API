from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from src.apps.blog.models import BlogTopic
from src.utils.db import filter_objects

User = get_user_model()


def get_available_blog_topics(user: User = None) -> QuerySet[BlogTopic]:
    return filter_objects(
        BlogTopic,
        is_hidden=False,
    ) | filter_objects(
        BlogTopic,
        creator=user,
    )
