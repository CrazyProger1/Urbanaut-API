from django.conf import settings
from rest_framework import views, response, status

from src.apps.accounts.serializers import LanguageListSerializer


class LanguageListAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        serializer = LanguageListSerializer(instance=settings.LANGUAGES, many=True)
        return response.Response({"results": serializer.data}, status=status.HTTP_200_OK)
