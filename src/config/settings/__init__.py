from split_settings.tools import include
from dotenv import load_dotenv

load_dotenv()

include(
    "base.py",
    "databases.py",
    "i18n.py",
    "celery.py",
    "logging.py",
    "cors.py",
    "docs.py",
    "auth.py",
    "rest.py",
    "media.py",
    "permissions.py",
    "unfold.py",
    "telegram.py",
    "kafka.py",
)
