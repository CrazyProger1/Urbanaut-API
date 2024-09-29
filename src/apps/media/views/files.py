from django.http import FileResponse
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins, permissions, parsers, status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from src.apps.media.permissions import IsFileOwnerOrReadOnly
from src.apps.media.services.db import get_user_files, get_unhidden_files
from src.apps.media.serializers import (
    FileRetrieveSerializer,
    FileListSerializer,
    FileCreateSerializer,
)
from src.apps.media.filters import FileFilter


class FileViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    queryset = get_unhidden_files()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsFileOwnerOrReadOnly)
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = FileListSerializer
    serializer_classes = {
        "retrieve": FileRetrieveSerializer,
        "create": FileCreateSerializer,
        "list": FileListSerializer
    }
    filterset_class = FileFilter

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset | get_user_files(user=self.request.user)

        return self.queryset

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)

    @extend_schema(
        request=FileCreateSerializer,
        responses={
            201: FileRetrieveSerializer
        },
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        response_serializer = FileRetrieveSerializer(instance)
        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        methods=["GET"],
        request=serializers.Serializer,
        responses=None
    )
    @action(
        detail=True,
        methods=("GET",),
        url_path="src",
    )
    def src(self, request, pk=None):
        file = self.get_object()
        file_handle = file.file
        response = FileResponse(
            file_handle.open("rb"),
            as_attachment=True,
            filename=file_handle.name
        )
        return response
