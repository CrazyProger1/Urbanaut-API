import hashlib
import json
from typing import Callable
from django.core.cache import cache


def func_cache(prefix: str = None, exp: int | None = 60):
    def decorator(target: Callable):
        def wrapper(*args, **kwargs):
            raw_key = f"{prefix or ''}{target.__name__}({json.dumps([args, kwargs], sort_keys=True)})"
            key = hashlib.sha256(raw_key.encode()).hexdigest()
            response = cache.get(key)

            if response:
                return response

            response = target(*args, **kwargs)
            cache.set(key, response, exp)
            return response

        return wrapper

    return decorator
