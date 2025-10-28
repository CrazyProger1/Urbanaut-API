from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from src.config.settings.base import INSTALLED_APPS

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",
    "unfold.contrib.guardian",
    "unfold.contrib.simple_history",
    *INSTALLED_APPS,
]

UNFOLD = {
    "SITE_TITLE": "Urbanaut",
    "SITE_HEADER": "Urbanaut",
    "SITE_URL": "/docs",
    "SITE_SYMBOL": "speed",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "THEME": "dark",
    "SITE_LOGO": {
        "light": lambda request: static("favicon.svg"),
        "dark": lambda request: static("favicon.svg"),
    },
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("favicon.svg"),
        },
    ],
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": _("Accounts"),
                "collapsible": False,
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "person",
                        "link": reverse_lazy("admin:accounts_user_changelist"),
                    },
                    {
                        "title": _("Achievements"),
                        "icon": "diamond",
                        "link": reverse_lazy("admin:accounts_achievement_changelist"),
                    },
                    {
                        "title": _("Groups"),
                        "icon": "devices",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
            {
                "title": _("Abandoned"),
                "collapsible": True,
                "items": [
                    {
                        "title": _("Places"),
                        "icon": "location_on",
                        "link": reverse_lazy("admin:abandoned_place_changelist"),
                    },
                    {
                        "title": _("Areas"),
                        "icon": "explore_nearby",
                        "link": reverse_lazy("admin:abandoned_area_changelist"),
                    },
                ],
            },
            {
                "title": _("Tags"),
                "collapsible": True,
                "items": [
                    {
                        "title": _("Tags"),
                        "icon": "tag",
                        "link": reverse_lazy("admin:tags_tag_changelist"),
                    },
                ],
            },
        ],
    },
}
