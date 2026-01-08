import logging

from django.conf import LazySettings

logger = logging.getLogger(__name__)


class DefaultSettings(LazySettings):

    def setdefault(self, key: str, default: any = None):
        return self.__dict__.setdefault(key, default)

    def __getattr__(self, item):
        try:
            return super().__getattr__(item)
        except AttributeError:
            logger.error("Can't find settings %s value or default value", item)
            raise AttributeError(
                f"Django settings doesn't contain {item} value or default value, "
                f"make sure you specify it in settings.py"
            )


default_settings = DefaultSettings()
