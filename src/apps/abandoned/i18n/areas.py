from modeltranslation.translator import TranslationOptions, translator
from simple_history import register

from src.apps.abandoned.models import AbandonedArea


class AbandonedAreaTranslationOptions(TranslationOptions):
    fields = ("name", "description")


translator.register(AbandonedArea, AbandonedAreaTranslationOptions)
register(AbandonedArea)
