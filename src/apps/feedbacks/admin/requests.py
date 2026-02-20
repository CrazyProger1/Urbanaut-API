from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.http import HttpRequest
from unfold.admin import ModelAdmin
from unfold.decorators import action

from src.apps.accounts.sites import site
from src.apps.feedbacks.models import Request
from src.apps.feedbacks.services.db import mark_request_fulfilled


@admin.register(Request, site=site)
class RequestAdmin(ModelAdmin):
    list_display = (
        "id",
        "is_fulfilled",
        "fulfilled_by",
        "fulfilled_at",
    )

    actions_submit_line = ("mark_fulfilled",)

    @action(
        description=_("Mark fulfilled"),
    )
    def mark_fulfilled(self, request: HttpRequest, obj: Request):
        mark_request_fulfilled(request=obj, user=request.user)
