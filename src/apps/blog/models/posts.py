from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from src.apps.media.enums import FileType
from src.apps.permissions.managers import PermissionManager
from src.apps.permissions.models import PermissionBaseModel
from src.utils.db.models import TimestampModelMixin

User = get_user_model()


class PostFile(models.Model):
    class Meta:
        verbose_name = _("file")
        verbose_name_plural = _("files")

    file = models.ForeignKey(
        "media.File",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        "BlogPost",
        on_delete=models.CASCADE,
    )
    priority = models.IntegerField(
        default=0,
    )


class BlogPost(TimestampModelMixin, PermissionBaseModel):
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    topic = models.ForeignKey(
        "BlogTopic",
        on_delete=models.CASCADE,
        verbose_name=_("topic"),
        help_text=_("Topic of the post."),
        blank=False,
        null=False,
    )
    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Title of the blog post."),
        max_length=250,
        null=False,
        blank=False,
    )
    summary = models.CharField(
        verbose_name=_("summary"),
        help_text=_("Brief summary of the post for the posts page."),
        null=False,
        blank=False,
    )
    content = models.TextField(
        verbose_name=_("content"),
        help_text=_("Content of the blog post."),
        null=False,
        blank=False,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="blog_posts",
        blank=True,
        null=True,
        verbose_name=_("created by"),
        help_text=_("Creator of the blog post."),
    )
    published_at = models.DateTimeField(
        verbose_name=_("published at"),
        help_text=_("Post published (or planned publishing) date and time."),
        default=timezone.now,
        blank=False,
        null=False,
    )
    files = models.ManyToManyField(
        "media.File",
        through=PostFile,
        verbose_name=_("files"),
        related_name="posts",
        help_text=_("The media files attached to this blog post."),
    )

    def photo(self):
        photo = self.files.filter(type=FileType.PHOTO).first()
        if photo:
            return photo.src

    def __str__(self):
        return self.title
