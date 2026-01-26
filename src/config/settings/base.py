from pathlib import Path
from decouple import config, Csv

APPLICATION = "Urbanaut"
DESCRIPTION = "Urbanaut-Club — a social platform for urban explorers, diggers, and extreme tourism enthusiasts."
VERSION = "0.0.2"

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
BASE_URL = config("BASE_URL", cast=str, default="http://localhost:8000")
BASE_FRONTEND_URL = config(
    "BASE_FRONTEND_URL", cast=str, default="http://localhost:3000"
)
SECRET_KEY = config("SECRET_KEY", cast=str)
DEBUG = config("DEBUG", cast=bool, default=False)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv(), default=["*"])

INSTALLED_APPS = [
    "daphne",
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "unfold.contrib.location_field",
    "unfold.contrib.constance",
    "django.contrib.postgres",
    "django_filters",
    "djoser",
    "cities_light",
    "django_celery_beat",
    "constance",
    "src.apps.docs",
    "src.apps.accounts",
    "src.apps.abandoned",
    "src.apps.tags",
    "src.apps.feedbacks",
    "src.apps.geo",
    "src.apps.media",
    "src.apps.notifications",
    "src.apps.config",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "src.apps.accounts.middlewares.Admin2FAMiddleware",
]

ROOT_URLCONF = "src.config.web.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "src.config.web.wsgi.application"
ASGI_APPLICATION = "src.config.web.asgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOCATION_FIELD = {
    "default_zoom": 12,
    "provider.openstreetmap": True,
    "search_by_default": True,
}
