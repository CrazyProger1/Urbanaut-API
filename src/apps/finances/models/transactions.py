import logging
import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from src.apps.finances.exceptions import AlreadySignedError


class Transaction(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    destination = models.JSONField(
        verbose_name=_("destination"),
        null=True,
        blank=True,
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
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        help_text=_("Creation date and time."),
        default=timezone.now,
        null=False,
        blank=False,
    )

    def _sign(self):
        logging.info("Signing transaction...")
        from src.apps.finances.services.db import get_last_transaction
        from src.apps.finances.services.sign import calculate_signature

        if self.signature:
            raise AlreadySignedError("Transaction is already signed")

        current_time = timezone.now()

        previous_transaction = get_last_transaction()
        self.signature = calculate_signature(
            balance_in_pk=self.balance_in.pk,
            balance_out_pk=self.balance_out.pk,
            amount=self.amount,
            timestamp=current_time.timestamp(),
            previous_signature=(
                previous_transaction.signature
                if previous_transaction
                else settings.INITIAL_SIGNATURE
            ),
            pk=self.pk,
        )
        self.created_at = current_time
        logging.info(
            "Transaction (amount = %s, balance_in = %s, balance_out = %s) signature generated: %s",
            self.amount,
            self.balance_in.pk,
            self.balance_out.pk,
            self.signature,
        )

    def is_valid(self, chain: bool = False) -> bool:
        from src.apps.finances.services.db import get_previous_transaction
        from src.apps.finances.services.sign import verify

        previous_transaction = get_previous_transaction(transaction=self)

        if (
            chain
            and previous_transaction
            and not previous_transaction.is_valid(chain=True)
        ):
            return False

        return verify(
            signature=self.signature,
            amount=self.amount,
            balance_in_pk=self.balance_in.pk,
            balance_out_pk=self.balance_out.pk,
            previous_signature=(
                previous_transaction.signature
                if previous_transaction
                else settings.INITIAL_SIGNATURE
            ),
            timestamp=self.created_at.timestamp(),
            pk=self.pk,
        )

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.signature:
            self._sign()

        super().save(*args, **kwargs)

        logging.info("Transaction commited: %s - %s", self.pk, self.signature)
