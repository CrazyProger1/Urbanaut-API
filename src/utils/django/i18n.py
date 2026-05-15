from django.conf import settings
from django.utils import translation
from django.utils.translation import gettext as _


def localize_field(field: str, value: str, **kwargs) -> dict:
    result = {}
    for lang_code, _lang_name in settings.LANGUAGES:
        with translation.override(lang_code):
            translated = _(value)
            result[f"{field}_{lang_code}"] = translated % kwargs if kwargs else translated
    return result
