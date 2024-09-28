from django.http import FileResponse
from rest_framework import viewsets, mixins, permissions
from rest_framework.decorators import action

from src.apps.media.services.db import get_all_files
from src.apps.media.serializers import FileListSerializer


class FileViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    queryset = get_all_files()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = FileListSerializer

    @action(
        detail=True,
        methods=("GET",),
        url_path="download",
    )
    def download(self, request, pk=None):
        file = self.get_object()
        file_handle = file.file
        response = FileResponse(
            file_handle.open("rb"),
            as_attachment=True,
            filename=file_handle.name
        )
        return response
