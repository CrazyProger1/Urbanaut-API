from rest_framework import viewsets, response, status, exceptions
from rest_framework.decorators import action

from src.apps.accounts.serializers import TermsRetrieveSerializer
from src.apps.accounts.services.db import get_all_terms, get_current_terms


class TermsViewSet(
    viewsets.GenericViewSet,
):
    queryset = get_all_terms()
    serializer_class = TermsRetrieveSerializer

    @action(methods=("GET",), detail=False, url_path="current")
    def current_terms(self, request):
        current = get_current_terms()

        if not current:
            raise exceptions.NotFound(detail="Current terms not found")

        serializer = self.serializer_class(current, many=False)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)
