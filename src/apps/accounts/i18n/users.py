from modeltranslation.translator import TranslationOptions, translator
from simple_history import register

from src.apps.accounts.models import User


class UserTranslationOptions(TranslationOptions):
    pass


translator.register(User, UserTranslationOptions)
register(User)
