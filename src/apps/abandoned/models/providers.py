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
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Description of the provider."),
        null=True,
        blank=True,
    )
