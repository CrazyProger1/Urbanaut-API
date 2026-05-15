import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.django.db import CreatedAtMixin


class ExperienceTransaction(CreatedAtMixin, models.Model):
    class Meta:
        verbose_name = _("Experience Transaction")
        verbose_name_plural = _("Experience Transactions")

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    amount = models.PositiveBigIntegerField(
        verbose_name=_("amount"),
        null=False,
        blank=False,
        default=0,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="experience_transactions",
    )


class ExperienceMixin(models.Model):
    class Meta:
        abstract = True

    @property
    def experience(self):
        return self.experience_transactions.aggregate(models.Sum("amount"))["amount__sum"] or 0
