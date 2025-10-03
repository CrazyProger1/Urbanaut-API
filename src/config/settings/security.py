from decouple import config, Csv

from src.config.settings.base import MIDDLEWARE, INSTALLED_APPS

INSTALLED_APPS += ["corsheaders"]

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
CSRF_TRUSTED_ORIGINS = config(
    "CSRF_TRUSTED_ORIGINS",
    cast=Csv(),
    default="http://localhost:8000",
)

MIDDLEWARE.insert(
    MIDDLEWARE.index("django.middleware.common.CommonMiddleware") - 1,
    "corsheaders.middleware.CorsMiddleware",
)

CORS_ALLOWED_ORIGINS = config(
    "CORS_ALLOWED_ORIGINS",
    cast=Csv(),
    default=["*"],
)
CORS_ALLOW_ALL_ORIGINS = config(
    "CORS_ALLOW_ALL_ORIGINS",
    cast=bool,
    default=False,
)
