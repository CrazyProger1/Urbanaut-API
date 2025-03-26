from modeltranslation.translator import TranslationOptions, translator
from simple_history import register

from src.apps.abandoned.models import AbandonedObject


class AbandonedObjectTranslationOptions(TranslationOptions):
    fields = ("name", "description", "short_description")


translator.register(AbandonedObject, AbandonedObjectTranslationOptions)
register(AbandonedObject)
