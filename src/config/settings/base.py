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
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
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
    "django_celery_beat",
    "drf_spectacular",
    "drf_standardized_errors",
    "mdeditor",
    "src.apps.accounts.apps.AccountsConfig",
    "src.apps.abandoned.apps.AbandonedConfig",
    "src.apps.media.apps.MediaConfig",
    "src.apps.docs.apps.DocsConfig",
    "src.apps.geo.apps.GeoConfig",
    "src.apps.notifications.apps.NotificationsConfig",
    "src.apps.actions.apps.ActionsConfig",
    "src.apps.blog.apps.BlogConfig",
    "src.apps.permissions.apps.PermissionsConfig",
    "src.apps.dashboard.apps.DashboardConfig",
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
