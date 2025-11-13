import json
from typing import Callable
from django.core.cache import cache


def redcache(prefix: str = None, exp: int = 60):
    def decorator(target: Callable):
        def wrapper(*args, **kwargs):
            key = f"{prefix or ''}{target.__name__}({json.dumps([args, kwargs])})"
            response = cache.get(key)

            if response:
                return response

            response = target(*args, **kwargs)
            cache.set(key, response, exp)
            return response

        return wrapper

    return decorator
