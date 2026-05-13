import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.django.db import CreatedAtMixin


class KarmaTransaction(CreatedAtMixin, models.Model):
    class Meta:
        verbose_name = _("Karma Transaction")
        verbose_name_plural = _("Karma Transactions")

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    amount = models.BigIntegerField(
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
        related_name="karma_transactions",
    )


class KarmaMixin(models.Model):
    class Meta:
        abstract = True

    @property
    def karma(self):
        return self.karma_transactions.aggregate(models.Sum("amount"))["amount__sum"]
