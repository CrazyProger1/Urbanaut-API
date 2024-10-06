from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(http_method_names=("GET",))
def get_languages(request, *args, **kwargs):
    return Response(
        dict(settings.LANGUAGES),
        status=status.HTTP_200_OK,
    )
