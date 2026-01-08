from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.django.db import CreatedAtMixin


class Feedback(CreatedAtMixin, models.Model):
    content = models.TextField(
        verbose_name=_("content"),
        blank=False,
        null=False,
        help_text=_("The content of the feedbacks"),
    )
