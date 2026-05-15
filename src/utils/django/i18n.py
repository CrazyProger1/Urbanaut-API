from django.conf import settings
from django.utils import translation
from django.utils.translation import gettext as _


def localize(value: str, **kwargs) -> dict:
    result = {}
    for lang_code, _lang_name in settings.LANGUAGES:
        with translation.override(lang_code):
            translated = _(value)
            result[lang_code] = translated % kwargs if kwargs else translated
    return result
