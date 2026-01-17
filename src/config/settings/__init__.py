from split_settings.tools import include, optional

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

include(
    "base.py",
    "auth.py",
    "databases.py",
    "i18n.py",
    "logging.py",
    "security.py",
    "ai.py",
    "cache.py",
    "achievements.py",
    "geo.py",
    "media.py",
    "celery.py",
    "channels.py",
    optional("rest.py"),
    optional("docs.py"),
    optional("unfold.py"),
)
