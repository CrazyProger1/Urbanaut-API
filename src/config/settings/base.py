from pathlib import Path

from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
BASE_URL = config("BASE_URL", cast=str, default="http://localhost:8001")

SECRET_KEY = config("SECRET_KEY", cast=str)

DEBUG = config("DEBUG", cast=bool, default=False)

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8001",
    "https://api.urbanaut.club",
]

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",
    "unfold.contrib.guardian",
    "unfold.contrib.simple_history",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "modeltranslation",
    "corsheaders",
    "cities",
    "rest_framework",
    "django_filters",
    "simple_history",
    "django_celery_beat",
    "drf_spectacular",
    "drf_standardized_errors",
    "mdeditor",
    "src.apps.accounts.apps.AccountsConfig",
    "src.apps.abandoned.apps.AbandonedConfig",
    "src.apps.media.apps.MediaConfig",
    "src.apps.docs.apps.DocsConfig",
    "src.apps.geo.apps.GeoConfig",
    "src.apps.notifier.apps.NotifierConfig",
    "src.apps.actions.apps.ActionsConfig",
    "src.apps.blog.apps.BlogConfig",
    "src.apps.permissions.apps.PermissionsConfig",
    "src.apps.dashboard.apps.DashboardConfig",
    "src.apps.ratings.apps.RatingsConfig",
    "src.apps.triggers.apps.TriggersConfig",
]

MIDDLEWARE = [
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    "simple_history.middleware.HistoryRequestMiddleware",

    "src.apps.accounts.middlewares.I18NMiddleware",
    "src.apps.dashboard.middlewares.Admin2FAMiddleware",
]

ROOT_URLCONF = "src.config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "src.config.wsgi.application"
ASGI_APPLICATION = "src.config.asgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

STATIC_URL = "static/"
STATIC_ROOT = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TITLE = "Urbanaut"
DESCRIPTION = "Urbanaut API Server"
VERSION = "0.0.1"
