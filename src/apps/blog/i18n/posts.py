from modeltranslation.translator import TranslationOptions, translator

from src.apps.blog.models import BlogPost


class BlogPostTranslationOptions(TranslationOptions):
    fields = ("name", "content")


translator.register(BlogPost, BlogPostTranslationOptions)
