from rest_framework import viewsets, permissions, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from src.apps.accounts.serializers import ReferralCodeListSerializer, ReferralCodeApplySerializer
from src.apps.accounts.services.db import (
    get_all_referral_codes,
    get_user_referral_codes,
    apply_referral_code,
    can_apply_referral_code,
)


class ReferralCodeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = get_all_referral_codes()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "code"
    serializer_class = ReferralCodeListSerializer
    serializer_classes = {
        "list": ReferralCodeListSerializer,
        "apply": ReferralCodeApplySerializer,
    }

    def get_queryset(self):
        if self.action == "list":
            return get_user_referral_codes(self.request.user)
        return super().get_queryset()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    @action(detail=True, methods=["post"])
    def apply(self, request, code=None):
        code = self.get_object()

        user = request.user

        if not can_apply_referral_code(code=code, user=user):
            return Response(status=status.HTTP_403_FORBIDDEN)

        apply_referral_code(code=code, user=user)
        return Response(status=status.HTTP_200_OK)
