from modeltranslation.translator import TranslationOptions, translator

from src.apps.notifications.models import Notification


class NotificationTranslationOptions(TranslationOptions):
    fields = ("title", "message")


translator.register(Notification, NotificationTranslationOptions)
