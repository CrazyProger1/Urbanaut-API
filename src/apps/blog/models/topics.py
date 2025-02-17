from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from src.apps.permissions.models import PermissionBaseModel

User = get_user_model()


class BlogTopic(PermissionBaseModel):
    class Meta:
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")

    name = models.CharField(
        max_length=250,
        verbose_name=_("name"),
        help_text=_("Name of the blog topic."),
        null=False,
        blank=False,
    )

    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Description of the blog topic."),
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        help_text=_("Topic creation date and time."),
        default=timezone.now,
    )
    is_closed = models.BooleanField(
        verbose_name=_("closed"),
        help_text=_("General user can't post to this topic."),
        default=False,
        null=False,
        blank=False,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="blog_topics",
        blank=True,
        null=True,
        verbose_name=_("created by"),
        help_text=_("Creator of the blog post."),
    )

    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"
