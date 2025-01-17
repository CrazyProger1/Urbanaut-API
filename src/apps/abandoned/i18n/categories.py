from modeltranslation.translator import TranslationOptions, translator

from src.apps.abandoned.models import Category


class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", "description",)


translator.register(Category, CategoryTranslationOptions)
