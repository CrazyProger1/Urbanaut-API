from rest_framework import (
    viewsets,
    mixins,
    permissions,
)

from src.apps.accounts.serializers import (
    ReferralLinkListSerializer,
    ReferralLinkRetrieveSerializer,
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

    def get_serializer_class(self):
        match self.action:
            case "list":
                return ReferralLinkListSerializer
            case "retrieve":
                return ReferralLinkRetrieveSerializer
        return self.serializer_class

    def get_queryset(self):
        return get_user_referral_links(self.request.user)
