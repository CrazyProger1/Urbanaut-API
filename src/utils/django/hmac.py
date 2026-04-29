import hmac


def _canonicalize(
        method: str,
        url: str,
        payload: bytes,
) -> bytes:
    parts = [
        method.upper().encode(),
        url.encode(),
        payload,
    ]
    return b"".join(len(p).to_bytes(8, "big") + p for p in parts)


def get_signature(
        key: bytes,
        method: str,
        url: str,
        payload: bytes,
) -> bytes:
    return hmac.new(
        key, _canonicalize(method, url, payload), "SHA256"
    ).digest()


def verify_signature(
        key: bytes,
        signature: bytes,
        method: str,
        url: str,
        payload: bytes,
) -> bool:
    expected = hmac.new(
        key, _canonicalize(method, url, payload), "SHA256"
    ).digest()
    return hmac.compare_digest(expected, signature)


