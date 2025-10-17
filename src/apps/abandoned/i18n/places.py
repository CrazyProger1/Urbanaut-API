from modeltranslation.translator import TranslationOptions, translator

from src.apps.abandoned.models import Place


class PlaceTranslationOptions(TranslationOptions):
    fields = ("name", "description")


translator.register(Place, PlaceTranslationOptions)
