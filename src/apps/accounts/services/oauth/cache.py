from django.core.cache import cache as django_cache


def _generate_google_oauth_cache_key(token: str) -> str:
    return f"google:oauth:{token}"


def save_google_oauth_cache(token: str, cache: dict):
    key = _generate_google_oauth_cache_key(token=token)
    django_cache.set(key, cache, timeout=600)


def load_google_oauth_cache(token: str) -> dict:
    key = _generate_google_oauth_cache_key(token=token)
    return django_cache.get(key) or {}
