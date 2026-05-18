from rest_framework import viewsets, permissions, mixins

from src.apps.accounts.serializers import ReferralCodeListSerializer, ReferralListSerializer
from src.apps.accounts.services.db import (
    get_all_referral_codes,
    get_user_referral_codes,
    get_user_referrals,
    get_all_referrals,
)


class ReferralCodeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = get_all_referral_codes()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "code"
    serializer_class = ReferralCodeListSerializer

    def get_queryset(self):
        return get_user_referral_codes(self.request.user)


class ReferralsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = get_all_referrals()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReferralListSerializer

    def get_queryset(self):
        return get_user_referrals(user=self.request.user)
