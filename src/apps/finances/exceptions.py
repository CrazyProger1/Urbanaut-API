class TransactionError(RuntimeError):
    pass


class AlreadySignedError(TransactionError):
    pass


class BalanceOutError(TransactionError):
    pass


class TransactionChainInvalidError(TransactionError):
    pass
