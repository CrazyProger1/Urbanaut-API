from src.apps.finances.models import Transaction


def get_previous_transaction(transaction: Transaction) -> Transaction | None:
    return Transaction.objects.order_by("-created_at").filter(created_at__lt=transaction.created_at).first()


def get_last_transaction() -> Transaction:
    return Transaction.objects.order_by("-created_at").first()
