from django.utils.translation import gettext as _
from rest_framework import (
    viewsets,
    mixins,
    permissions,
    response,
)
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied

from src.apps.accounts.serializers import (
    ReferralLinkListSerializer,
    ReferralLinkRetrieveSerializer,
    ReferralLinkApplySerializer,
    ReferralUserListSerializer,
)
from src.apps.accounts.services.db import (
    get_all_referral_links,
    get_user_referral_links,
    get_non_user_referral_links,
    apply_referral_link,
    get_all_users,
    get_user_referrals,
)


class ReferralLinkViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_all_referral_links()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReferralLinkListSerializer
    serializer_classes = {
        "list": ReferralLinkListSerializer,
        "retrieve": ReferralLinkRetrieveSerializer,
        "apply": ReferralLinkApplySerializer,
    }
    lookup_field = "code"

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        if self.action == "apply":
            return get_non_user_referral_links(user=self.request.user)

        return get_user_referral_links(user=self.request.user)

    @action(
        methods=("POST",),
        detail=True,
        url_path="apply",
    )
    def apply(self, request, *args, **kwargs):
        link = self.get_object()
        user = request.user
        is_applied = apply_referral_link(
            user=user,
            link=link,
        )
        if not is_applied:
            raise PermissionDenied(_("You have already applied referral link."))

        return response.Response(
            status=200,
            data={
                "detail": _("Referral link applied successfully."),
            },
        )


class ReferralViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = get_all_users()
    serializer_classes = {
        "list": ReferralUserListSerializer,
    }
    serializer_class = ReferralUserListSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return get_user_referrals(user=self.request.user)
