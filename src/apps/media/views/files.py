from django.http import FileResponse
from rest_framework import viewsets, mixins, permissions
from rest_framework.decorators import action

from src.apps.media.permissions import IsFileOwnerOrReadOnly
from src.apps.media.services.db import get_user_files, get_unhidden_files
from src.apps.media.serializers import FileRetrieveSerializer, FileListSerializer


class FileViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    queryset = get_unhidden_files()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsFileOwnerOrReadOnly)
    serializer_class = FileListSerializer

    def get_serializer_class(self):
        match self.action:
            case "retrieve":
                return FileRetrieveSerializer
            case "list":
                return FileListSerializer

        return self.serializer_class

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset & get_user_files(user=self.request.user)

        return self.queryset

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
