from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.decorators import action

from src.apps.accounts.sites import site
from src.apps.finances.models import Transaction


@admin.register(Transaction, site=site)
class TransactionAdmin(ModelAdmin):
    list_display = ("balance_out", "balance_in", "amount", "is_valid", "created_at")
    readonly_fields = (
        "signature",
        "is_valid",
    )

    def is_valid(self, transaction: Transaction) -> bool:
        return True

    is_valid.short_description = "Valid"
