from modeltranslation.translator import TranslationOptions, translator

from src.apps.abandoned.models import AbandonedArea


class AbandonedAreaTranslationOptions(TranslationOptions):
    pass


translator.register(AbandonedArea, AbandonedAreaTranslationOptions)
