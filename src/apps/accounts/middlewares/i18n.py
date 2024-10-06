import logging

from django.utils import translation
from django.conf import settings

logger = logging.getLogger(__name__)


class I18NMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        accept_language = request.headers.get("Accept-Language", settings.LANGUAGE_CODE)

        if request.user.is_authenticated and hasattr(request.user, "language"):
            translation.activate(request.user.language)
        else:
            translation.activate(accept_language)

        request.LANGUAGE_CODE = translation.get_language()

        logger.debug(f"Set language: {request.LANGUAGE_CODE}")

        response = self.get_response(request)

        translation.deactivate()

        return response
