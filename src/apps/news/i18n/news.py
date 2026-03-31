from modeltranslation.translator import TranslationOptions, translator

from src.apps.news.models import News


class NewsTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "content")


translator.register(News, NewsTranslationOptions)
