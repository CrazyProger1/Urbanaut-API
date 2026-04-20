import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.django.db import CreatedAtMixin


class Transaction(CreatedAtMixin, models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    balance_in = models.ForeignKey(
        to="Balance",
        on_delete=models.CASCADE,
        related_name="transactions_in",
        null=False,
        blank=False,
    )
    balance_out = models.ForeignKey(
        to="Balance",
        on_delete=models.CASCADE,
        related_name="transactions_out",
        null=False,
        blank=False,
    )
    amount = models.PositiveBigIntegerField(
        verbose_name=_("amount"),
        null=False,
        blank=False,
        default=0,
    )
    signature = models.CharField(
        verbose_name=_("signature"),
        max_length=255,
        null=False,
        blank=False,
    )
