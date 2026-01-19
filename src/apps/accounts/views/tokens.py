from rest_framework import (
    generics,
    permissions,
    response,
    status,
)

from src.apps.accounts.serializers import WebsocketTokenObtainSerializer
from src.apps.accounts.services.websockets import generate_websocket_token


class WebsocketTokenCreateView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = WebsocketTokenObtainSerializer

    def post(self, request, *args, **kwargs):
        token = generate_websocket_token(user=request.user)
        serializer = self.get_serializer(instance={"token": token})
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
