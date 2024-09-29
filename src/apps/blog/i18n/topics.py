from modeltranslation.translator import TranslationOptions, translator

from src.apps.blog.models import BlogTopic


class BlogTopicTranslationOptions(TranslationOptions):
    fields = ("name", "description")


translator.register(BlogTopic, BlogTopicTranslationOptions)
