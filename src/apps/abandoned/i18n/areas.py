from modeltranslation.translator import TranslationOptions, translator

from src.apps.abandoned.models import Area


class AreaTranslationOptions(TranslationOptions):
    fields = ("name", "description")


translator.register(Area, AreaTranslationOptions)
