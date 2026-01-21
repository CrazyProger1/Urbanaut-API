from unfold.contrib.constance.settings import UNFOLD_CONSTANCE_ADDITIONAL_FIELDS

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
