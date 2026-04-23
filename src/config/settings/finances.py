from decouple import config

INITIAL_SIGNATURE = config("INITIAL_SIGNATURE", cast=str, default="INSECURE_DEBUG_SIGNATURE")
