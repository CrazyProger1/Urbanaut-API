from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from src.apps.permissions.managers import PermissionManager
from src.apps.permissions.models import BasePermissionModel

User = get_user_model()


class BlogPost(BasePermissionModel):
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    topic = models.ForeignKey(
        "BlogTopic",
        on_delete=models.CASCADE,
        verbose_name=_("Topic"),
        help_text=_("Topic of the post."),
        blank=False,
        null=False,
    )
    is_hidden = models.BooleanField(
        verbose_name=_("Hidden"),
        help_text=_("Hidden from general users and available only for admins and creator."),
        default=False,
        null=False,
        blank=False,
    )
    title = models.CharField(
        verbose_name=_("Title"),
        help_text=_("Title of the blog post."),
        max_length=250,
        null=False,
        blank=False,
    )
    content = models.TextField(
        verbose_name=_("Content"),
        help_text=_("Content of the blog post."),
        null=False,
        blank=False,
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="blog_posts",
        blank=True,
        null=True,
        verbose_name=_("Creator"),
        help_text=_("Creator of the blog post."),
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        help_text=_("Post creation date and time."),
        default=timezone.now,
        blank=False,
        null=False,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        help_text=_("Post updated date and time."),
        auto_now=True,
        blank=False,
        null=False,
    )
    published_at = models.DateTimeField(
        verbose_name=_("Published At"),
        help_text=_("Post published (or planned publishing) date and time."),
        default=timezone.now,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"
