from modeltranslation.translator import TranslationOptions, translator

from src.apps.accounts.models import User


class UserTranslationOptions(TranslationOptions):
    pass


translator.register(User, UserTranslationOptions)
