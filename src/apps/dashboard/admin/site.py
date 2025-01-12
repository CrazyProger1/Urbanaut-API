from django.shortcuts import redirect, render
from django.urls import reverse, path
from unfold.sites import UnfoldAdminSite

from src.utils.telegram import send_message


class AdvancedAdminSite(UnfoldAdminSite):
    admin_2fa_template = "2fa.html"
    admin_2fa_route = "2fa/"

    def login(self, request, extra_context=None):
        response = super().login(request, extra_context)
        # if request.method == "POST" and response.status_code == 302:
        #     return redirect(reverse("admin:admin_2fa"))
        return response

    # def admin_2fa_view(self, request):
    #     if request.method == "POST":
    #         code = request.POST.get("code")
    #         if code == "123456":
    #             return redirect(reverse("admin:index"))
    #         else:
    #             context = {"error": "Invalid 2FA code"}
    #             return render(request, self.admin_2fa_template, context)
    #     return render(request, self.admin_2fa_template)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = []
        # custom_urls = [
        #     path(self.admin_2fa_route, self.admin_view(self.admin_2fa_view), name="admin_2fa"),
        # ]
        return custom_urls + urls


site = AdvancedAdminSite(name="advanced-admin")
