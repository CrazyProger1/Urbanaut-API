from rest_framework import viewsets, permissions, mixins
from django_filters import rest_framework as filters

from src.apps.accounts.filters.referrals import ReferralFilter
from src.apps.accounts.serializers import (
    ReferralCodeListSerializer,
    ReferralListSerializer,
)
from src.apps.accounts.services.db import (
    get_all_referral_codes,
    get_user_referral_codes,
    get_all_referrals,
    get_user_referrals,
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
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ReferralFilter

    def get_queryset(self):
        if "referrer" not in self.request.query_params:
            return get_user_referrals(self.request.user)
        return get_all_referrals()
