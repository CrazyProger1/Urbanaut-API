from src.apps.finances.models import Transaction, Balance


def get_previous_transaction(transaction: Transaction) -> Transaction | None:
    return Transaction.objects.order_by("-created_at").filter(created_at__lt=transaction.created_at).first()


def get_last_transaction() -> Transaction | None:
    return Transaction.objects.order_by("-created_at").first()


def get_system_pool() -> Balance:
    return Balance.objects.get_or_create(is_pool=True)[0]

