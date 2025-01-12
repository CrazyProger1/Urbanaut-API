import logging

from django.shortcuts import redirect
from django.urls import reverse

logger = logging.getLogger(__name__)


class Admin2FAMiddleware:
    """
    Middleware to enforce 2FA for admin users.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_routes = (
            reverse("admin:login"),
            reverse("admin:admin_2fa"),
        )
        print(self.allowed_routes)

    def is_2fa_verified(self, request):
        return request.session.get("admin_2fa_verified", False)

    def __call__(self, request):
        if "admin" in request.path and not self.is_2fa_verified(request=request):
            if request.path not in self.allowed_routes:
                if request.user.is_authenticated:
                    return redirect(reverse("admin:admin_2fa"))
                else:
                    return redirect(reverse("admin:login"))
        return self.get_response(request)
