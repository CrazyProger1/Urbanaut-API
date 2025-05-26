from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CreatedAtMixin(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        help_text=_("Creation date and time."),
        default=timezone.now,
    )

    class Meta:
        abstract = True


class UpdatedAtMixin(models.Model):
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        help_text=_("Update date and time."),
        auto_now=True,
    )

    class Meta:
        abstract = True


class TimestampMixin(CreatedAtMixin, UpdatedAtMixin):
    class Meta:
        abstract = True
