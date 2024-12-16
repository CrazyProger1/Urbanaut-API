from modeltranslation.translator import TranslationOptions, translator

from src.apps.abandoned.models import AbandonedObjectCategory


class AbandonedObjectCategoryTranslationOptions(TranslationOptions):
    fields = ("name", "description",)


translator.register(AbandonedObjectCategory, AbandonedObjectCategoryTranslationOptions)
