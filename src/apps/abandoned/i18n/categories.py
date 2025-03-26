from modeltranslation.translator import TranslationOptions, translator
from simple_history import register

from src.apps.abandoned.models import Category


class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", "description",)


translator.register(Category, CategoryTranslationOptions)
register(Category)
