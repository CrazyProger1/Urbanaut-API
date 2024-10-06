from django.utils.translation import gettext_lazy as _

PERMISSION_GROUPS = (
    (0, _("SUPERUSERS")),
    (100, _("ADMINISTRATORS")),
    (200, _("OWNERS")),
    (300, _("AUTHENTICATED")),
    (400, _("EVERYONE")),
    (500, _("BANNED")),
)

PERMISSION_MODELS = (
    ("blog.BlogPost", _("Blog Posts")),
)
