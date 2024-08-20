from modeltranslation.translator import TranslationOptions, translator

from src.apps.abandoned.models import AbandonedObject


class AbandonedObjectTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(AbandonedObject, AbandonedObjectTranslationOptions)
