from telegram import Bot
from django.conf import settings


def send_message(chat_id: int, text: str):
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id, text)
