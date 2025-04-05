from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": "Urbanaut-API",
    "SITE_HEADER": "Urbanaut-API",
    "SITE_URL": "/docs",
    "SITE_SYMBOL": "speed",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "THEME": "dark",
    "COLORS": {
        "font": {
            "subtle-light": "107 114 128",
            "subtle-dark": "156 163 175",
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "17 24 39",
            "important-dark": "243 244 246",
        },
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "gb",
                "uk": "uk",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": _("Accounts"),
                "collapsible": True,
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "person",
                        "link": reverse_lazy("admin:accounts_user_changelist"),
                    },
                    {
                        "title": _("Ranks"),
                        "icon": "star",
                        "link": reverse_lazy("admin:accounts_rank_changelist"),
                    },
                    {
                        "title": _("Teams"),
                        "icon": "group",
                        "link": reverse_lazy("admin:accounts_team_changelist"),
                    },
                    {
                        "title": _("Groups"),
                        "icon": "devices",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                    {
                        "title": _("Referral Links"),
                        "icon": "link",
                        "link": reverse_lazy("admin:accounts_referrallink_changelist"),
                    },
                ],
            },
            {
                "title": _("Notifier"),
                "collapsible": True,
                "items": [
                    {
                        "title": _("Events"),
                        "icon": "event",
                        "link": reverse_lazy("admin:notifier_event_changelist"),
                    },
                    {
                        "title": _("Categories"),
                        "icon": "category",
                        "link": reverse_lazy("admin:notifier_category_changelist"),
                    },
                    {
                        "title": _("Notifications"),
                        "icon": "notifications",
                        "link": reverse_lazy("admin:notifier_notification_changelist"),
                    },
                    {
                        "title": _("Newsletters"),
                        "icon": "mail",
                        "link": reverse_lazy("admin:notifier_newsletter_changelist"),
                    },
                ],
            },
            {
                "title": _("Abandoned"),
                "collapsible": True,
                "items": [
                    {
                        "title": _("Categories"),
                        "icon": "category",
                        "link": reverse_lazy("admin:abandoned_category_changelist"),
                    },
                    {
                        "title": _("Objects"),
                        "icon": "person",
                        "link": reverse_lazy("admin:abandoned_abandonedobject_changelist"),
                    },
                    {
                        "title": _("Areas"),
                        "icon": "group",
                        "link": reverse_lazy("admin:abandoned_abandonedarea_changelist"),
                    },
                ],
            },
            {
                "title": _("Blog"),
                "collapsible": True,
                "items": [
                    {
                        "title": _("Topics"),
                        "icon": "topic",
                        "link": reverse_lazy("admin:blog_blogtopic_changelist"),
                    },
                    {
                        "title": _("Posts"),
                        "icon": "library_books",
                        "link": reverse_lazy("admin:blog_blogpost_changelist"),
                    },
                ],
            },
            {
                "title": _("Media"),
                "collapsible": True,
                "items": [
                    {
                        "title": _("Files"),
                        "icon": "attach_file",
                        "link": reverse_lazy("admin:media_file_changelist"),
                    },
                ],
            },
            {
                "title": _("Permissions"),
                "collapsible": True,
                "items": [
                    {
                        "title": _("Model Permission"),
                        "icon": "lock",
                        "link": reverse_lazy("admin:permissions_modelpermission_changelist"),
                    },
                    {
                        "title": _("User-Model Permission"),
                        "icon": "lock",
                        "link": reverse_lazy("admin:permissions_usermodelpermission_changelist"),
                    },
                    {
                        "title": _("Object Permission"),
                        "icon": "lock",
                        "link": reverse_lazy("admin:permissions_objectpermission_changelist"),
                    },
                    {
                        "title": _("User-Object Permission"),
                        "icon": "lock",
                        "link": reverse_lazy("admin:permissions_userobjectpermission_changelist"),
                    },
                ],
            },
        ],
    },
}
