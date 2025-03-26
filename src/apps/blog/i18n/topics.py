from modeltranslation.translator import TranslationOptions, translator
from simple_history import register

from src.apps.blog.models import BlogTopic


class BlogTopicTranslationOptions(TranslationOptions):
    fields = ("name", "description")


translator.register(BlogTopic, BlogTopicTranslationOptions)
register(BlogTopic)
