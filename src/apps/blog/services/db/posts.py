from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from src.apps.blog.models import BlogPost
from src.utils.db import filter_objects

User = get_user_model()


def get_available_blog_posts(user: User = None) -> QuerySet[BlogPost]:
    return BlogPost.objects.visible(user=user)


def count_user_blog_posts(user: User = None) -> int:
    return user.blog_posts.count()
