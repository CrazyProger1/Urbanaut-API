import pyotp


def create(key: str, name: str, app: str) -> str:
    totp = pyotp.TOTP(key)
    return totp.provisioning_uri(
        name=name,
        issuer_name=app,
    )


def verify(key: str, code: str) -> bool:
    totp = pyotp.TOTP(key)
    return totp.verify(code)
