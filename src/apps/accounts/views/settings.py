import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_spectacular.utils import extend_schema

from src.apps.accounts.serializers import SettingsUpdateSerializer
from src.apps.accounts.services.db import get_user_settings

logger = logging.getLogger(__name__)


class SettingsAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return get_user_settings(user=self.request.user)

    @extend_schema(
        request=SettingsUpdateSerializer,
        responses={200: SettingsUpdateSerializer},
        operation_id='update_user_settings',
        description="Fully update the authenticated user's settings.",
    )
    def put(self, request, *args, **kwargs):
        user = request.user
        user_settings = self.get_object()
        serializer = SettingsUpdateSerializer(user_settings, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            logger.debug("User %s updated settings: %s", user, serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=SettingsUpdateSerializer,
        responses={200: SettingsUpdateSerializer},
        operation_id='partial_update_user_settings',
        description="Partially update the authenticated user's settings.",
    )
    def patch(self, request, *args, **kwargs):
        user = request.user
        user_settings = self.get_object()
        serializer = SettingsUpdateSerializer(user_settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.debug("User %s updated settings: %s", user, serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
