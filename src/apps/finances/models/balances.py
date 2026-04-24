import logging
import uuid

from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

from src.utils.django.db import TimestampMixin

logger = logging.getLogger(__name__)


class Balance(TimestampMixin, models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    owned_by = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="balance",
        null=True,
        blank=True,
    )
    is_pool = models.BooleanField(
        verbose_name=_("pool"),
        default=False,
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = _("Balance")
        verbose_name_plural = _("Balances")

    def __str__(self):
        return f"{self.owned_by if self.owned_by else 'Pool'} ({str(self.id)[:10]})"


class BalanceMixin(models.Model):
    class Meta:
        abstract = True

    def _create_balance(self):
        if not self.pk or not hasattr(self, "balance"):
            balance = Balance.objects.create(owned_by=self)
            logger.info(
                f"Created balance instance ({balance.pk}) for new user ({self.pk})"
            )

    def save(self, *args, **kwargs):
        super().save(
            *args,
            **kwargs,
        )
        self._create_balance()

    @property
    def money(self) -> int:
        try:
            balance = self.balance
        except Balance.DoesNotExist:
            return 0
        payins = balance.transactions_in.aggregate(Sum("amount"))["amount__sum"] or 0
        payouts = balance.transactions_out.aggregate(Sum("amount"))["amount__sum"] or 0
        return payins - payouts
