from modeltranslation.translator import TranslationOptions, translator

from src.apps.abandoned.models import Place
from src.apps.tags.models import Tag


class TagTranslationOptions(TranslationOptions):
    fields = ("tag",)


translator.register(Tag, TagTranslationOptions)
