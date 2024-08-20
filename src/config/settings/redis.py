from decouple import config

REDIS_HOST = config("REDIS_HOST", default="localhost")
REDIS_PORT = config("REDIS_PORT", default="6379", cast=int)
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
