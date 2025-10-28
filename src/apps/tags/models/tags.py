from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.django.db import TimestampMixin


class Tag(TimestampMixin, models.Model):
    tag = models.SlugField(
        max_length=100,
        verbose_name=_("tag"),
        null=False,
        blank=False,
        db_index=True,
        unique=True,
    )

    def __str__(self):
        return self.tag
