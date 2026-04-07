from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.news.enums import NewsType
from src.apps.stats.models import ViewsMixin
from src.utils.django.db import CreatedAtMixin, UpdatedAtMixin


class News(ViewsMixin, CreatedAtMixin, UpdatedAtMixin, models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name=_("title"),
        blank=False,
        null=False,
    )
    subtitle = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name=_("subtitle"),
        help_text=_("Subtitle of the newsletter."),
    )
    content = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("content"),
        help_text=_("Newsletter content."),
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name=_("is published"),
        blank=False,
        null=False,
    )
    published_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("published at"),
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="news",
    )
    type = models.CharField(
        max_length=20,
        choices=NewsType,
        default=NewsType.SYSTEM,
        verbose_name=_("type"),
        help_text=_("Newsletter type."),
    )
    has_more = models.BooleanField(
        default=False,
        verbose_name=_("has more"),
        blank=False,
        null=False,
        help_text=_('Show "Read more" button on the newsletter.'),
    )

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

    def __str__(self):
        return self.title
