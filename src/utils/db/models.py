from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CreatedAtModelMixin(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        help_text=_("Creation date and time."),
        default=timezone.now,
    )

    class Meta:
        abstract = True


class UpdatedAtModelMixin(models.Model):
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        help_text=_("Update date and time."),
        auto_now=True,
    )

    class Meta:
        abstract = True


class TimestampModelMixin(CreatedAtModelMixin, UpdatedAtModelMixin):
    class Meta:
        abstract = True
