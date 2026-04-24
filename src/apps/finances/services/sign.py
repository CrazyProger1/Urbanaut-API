import hashlib
import hmac
import secrets


def calculate_signature(
    pk: str,
    balance_in_pk: str,
    balance_out_pk: str,
    amount: int,
    timestamp: float,
    previous_signature: str,
) -> str:
    salt = secrets.token_hex(16)
    raw = f"{pk}:{balance_in_pk}:{balance_out_pk}:{amount}:{previous_signature}:{timestamp}:{salt}".encode()
    digest = hmac.new(salt.encode(), raw, hashlib.sha256).hexdigest()
    return f"{salt}${digest}"


def verify(
    signature: str,
    pk: str,
    balance_in_pk: str,
    balance_out_pk: str,
    amount: int,
    timestamp: float,
    previous_signature: str,
) -> bool:
    try:
        salt, digest = signature.split("$", 1)
    except ValueError:
        return False
    raw = f"{pk}:{balance_in_pk}:{balance_out_pk}:{amount}:{previous_signature}:{timestamp}:{salt}".encode()
    expected = hmac.new(salt.encode(), raw, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, digest)
