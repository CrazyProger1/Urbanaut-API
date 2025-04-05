from rest_framework import (
    viewsets,
    mixins,
    permissions, response,
)
from rest_framework.decorators import action

from src.apps.accounts.serializers import (
    ReferralLinkListSerializer,
    ReferralLinkRetrieveSerializer, ReferralLinkApplySerializer,
)
from src.apps.accounts.services.db import (
    get_all_referral_links,
    get_user_referral_links,
)


class ReferralLinkViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_all_referral_links()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReferralLinkListSerializer
    lookup_field = "code"

    def get_serializer_class(self):
        match self.action:
            case "list":
                return ReferralLinkListSerializer
            case "retrieve":
                return ReferralLinkRetrieveSerializer
            case "apply":
                return ReferralLinkApplySerializer
        return self.serializer_class

    def get_queryset(self):
        return get_user_referral_links(self.request.user)

    @action(
        methods=("POST",),
        detail=True,
        url_path="apply",
    )
    def apply(self, request, *args, **kwargs):
        link = self.get_object()
        user = request.user
        return response.Response({"message": f"Referral link applied successfully! {link} by user {user}"})
