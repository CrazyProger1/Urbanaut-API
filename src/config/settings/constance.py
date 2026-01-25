from decouple import config
from unfold.contrib.constance.settings import UNFOLD_CONSTANCE_ADDITIONAL_FIELDS

from src.config.settings.cache import REDIS_HOST, REDIS_PORT

CONSTANCE_BACKEND = "constance.backends.redisd.RedisBackend"


CONSTANCE_REDIS_CONNECTION = {
    "host": REDIS_HOST,
    "port": REDIS_PORT,
    "db": 2,
}

CONSTANCE_CONFIG = {
    "MAINTENANCE": (
        False,
        "Site is under maintenance right now",
    ),
}

CONSTANCE_ADDITIONAL_FIELDS = {
    **UNFOLD_CONSTANCE_ADDITIONAL_FIELDS,
    "choice_field": [
        "django.forms.fields.ChoiceField",
        {
            "widget": "unfold.widgets.UnfoldAdminSelectWidget",
            "choices": (
                ("light-blue", "Light blue"),
                ("dark-blue", "Dark blue"),
            ),
        },
    ],
}
