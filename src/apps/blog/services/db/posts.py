from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from src.apps.blog.models import BlogPost
from src.utils.db import filter_objects

User = get_user_model()


def get_available_blog_posts(user: User = None) -> QuerySet[BlogPost]:
    return filter_objects(
        BlogPost,
        is_hidden=False,
        topic__is_hidden=False,
    ) | filter_objects(
        BlogPost,
        creator=user,
    )
