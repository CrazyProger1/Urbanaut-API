from modeltranslation.translator import TranslationOptions, translator
from simple_history import register

from src.apps.blog.models import BlogPost


class BlogPostTranslationOptions(TranslationOptions):
    fields = ("title", "content")


translator.register(BlogPost, BlogPostTranslationOptions)
register(BlogPost)
