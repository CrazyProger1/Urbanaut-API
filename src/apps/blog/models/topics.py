from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class BlogTopic(models.Model):
    class Meta:
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")

    name = models.CharField(
        max_length=250,
        verbose_name=_("Name"),
        help_text=_("Name of the blog topic."),
        null=False,
        blank=False,
    )

    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Description of the blog topic."),
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        help_text=_("Topic creation date and time."),
        default=timezone.now,
    )
    is_hidden = models.BooleanField(
        verbose_name=_("Hidden"),
        help_text=_("Hidden from general users and available only for admins and creator."),
        default=False,
        null=False,
        blank=False,
    )
    is_closed = models.BooleanField(
        verbose_name=_("Closed"),
        help_text=_("General user can't post to this topic."),
        default=False,
        null=False,
        blank=False,
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="blog_topics",
        blank=True,
        null=True,
        verbose_name=_("Creator"),
        help_text=_("Creator of the blog post."),
    )

    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"
