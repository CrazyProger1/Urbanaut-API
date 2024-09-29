from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BlogPost(models.Model):
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
    name = models.CharField(
        verbose_name=_("Name"),
        help_text=_("Name of the blog post."),
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
