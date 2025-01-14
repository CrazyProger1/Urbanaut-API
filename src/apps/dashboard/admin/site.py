from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse, path
from unfold.sites import UnfoldAdminSite

from src.utils.otp import verify


class AdvancedAdminSite(UnfoldAdminSite):
    admin_2fa_template = "2fa.html"
    admin_2fa_route = "2fa/"

    def login(self, request, extra_context=None):
        response = super().login(request, extra_context)
        if request.method == "POST" and response.status_code == 302:
            return redirect(reverse("admin:admin_2fa"))
        return response

    def admin_2fa_view(self, request):
        context = {}
        if request.method == "POST":
            code = request.POST.get("code")
            key = settings.SECRET_KEY + str(request.user.id)
            success = verify(key=key, code=code)
            if success:
                request.session["admin_2fa_verified"] = True
                return redirect(reverse("admin:index"))
            else:
                context["error"] = "Invalid 2FA code"
        return render(request, self.admin_2fa_template, context)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                self.admin_2fa_route,
                self.admin_view(self.admin_2fa_view),
                name="admin_2fa",
            ),
        ]
        return custom_urls + urls


site = AdvancedAdminSite(name="advanced-admin")
