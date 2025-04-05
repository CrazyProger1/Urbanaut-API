from decouple import config

TELEGRAM_BOT_TOKEN = config("TELEGRAM_BOT_TOKEN", cast=str)
TELEGRAM_RATE_PER_SECOND_SENDING = 30
