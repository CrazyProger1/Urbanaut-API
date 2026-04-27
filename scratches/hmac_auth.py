# METHOD + URL + PAYLOAD + TIMESTAMP + REQUEST_ID

import hmac
import json
import time
import uuid
from dataclasses import dataclass

SECRET_KEY = b"TEST"
REPLAY_WINDOW_SECONDS = 300

_seen_request_ids: dict[str, int] = {}


class SignatureError(Exception):
    pass


@dataclass
class Request:
    method: str
    url: str
    payload: dict
    timestamp: int
    request_id: str


def _canonicalize(request: Request) -> bytes:
    parts = [
        request.method.upper().encode(),
        request.url.encode(),
        json.dumps(request.payload, sort_keys=True, separators=(",", ":")).encode(),
        str(int(request.timestamp)).encode(),
        request.request_id.encode(),
    ]
    return b"".join(len(p).to_bytes(8, "big") + p for p in parts)


def get_signature(request: Request) -> bytes:
    return hmac.new(SECRET_KEY, _canonicalize(request), "SHA256").digest()


def _check_replay(request: Request, now: int) -> None:
    if abs(now - request.timestamp) > REPLAY_WINDOW_SECONDS:
        raise SignatureError("timestamp outside replay window")

    cutoff = now - REPLAY_WINDOW_SECONDS
    for rid, ts in list(_seen_request_ids.items()):
        if ts < cutoff:
            del _seen_request_ids[rid]

    if request.request_id in _seen_request_ids:
        raise SignatureError("request_id already used")
    _seen_request_ids[request.request_id] = request.timestamp


def verify_signature(request: Request, signature: bytes) -> bool:
    expected = hmac.new(SECRET_KEY, _canonicalize(request), "SHA256").digest()
    if not hmac.compare_digest(expected, signature):
        return False
    try:
        _check_replay(request, int(time.time()))
    except SignatureError:
        return False
    return True


def main():
    request = Request(
        method="GET",
        url="https://www.google.com",
        payload={"hello": "world"},
        timestamp=int(time.time()),
        request_id=str(uuid.uuid4()),
    )
    sign = get_signature(request)

    print(sign.hex())
    print(verify_signature(request, sign))
    print(verify_signature(request, sign))


if __name__ == "__main__":
    main()
