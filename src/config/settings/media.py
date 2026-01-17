from decouple import config

STATIC_URL = config("STATIC_URL", default="static/")
STATIC_ROOT = config("STATIC_ROOT", default="static/")
UPLOAD_ROOT = config("UPLOAD_ROOT", default="media/")
