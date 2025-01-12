from django.shortcuts import redirect
from django.urls import reverse


class Admin2FAMiddleware:
    admin_route = "admin/"
    """
    Middleware to enforce 2FA for admin users.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path.startswith(f"/{self.admin_route}"):
            if not request.session.get("admin_2fa_verified", False):
                if request.path != reverse("admin:admin_2fa"):
                    return redirect(reverse("admin:admin_2fa"))
        return self.get_response(request)
