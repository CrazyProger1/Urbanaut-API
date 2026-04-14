from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.django.db import CreatedAtMixin


class Provider(CreatedAtMixin, models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name=_("name"),
        help_text=_("Name of the provider."),
        null=False,
        blank=False,
    )
    slug = models.SlugField(
        max_length=250,
        verbose_name=_("slug"),
        help_text=_("Slug of the provider."),
        null=False,
        blank=False,
        unique=True,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Description of the provider."),
        null=True,
        blank=True,
    )
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("created by"),
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name
