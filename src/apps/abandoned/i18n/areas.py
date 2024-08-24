from modeltranslation.translator import TranslationOptions, translator

from src.apps.abandoned.models import AbandonedArea


class AbandonedAreaTranslationOptions(TranslationOptions):
    fields = ("name", "description")


translator.register(AbandonedArea, AbandonedAreaTranslationOptions)
