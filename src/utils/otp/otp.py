import base64

import pyotp


def create(key: str, name: str, app: str) -> str:
    base32_key = base64.b32encode(key.encode()).decode()
    totp = pyotp.TOTP(base32_key)
    return totp.provisioning_uri(
        name=name,
        issuer_name=app,
    )


def verify(key: str, code: str) -> bool:
    base32_key = base64.b32encode(key.encode()).decode()
    totp = pyotp.TOTP(base32_key)
    return totp.verify(code)
