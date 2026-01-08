from django.http import Http404
from djoser import signals as djoser_signals
from djoser.compat import get_user_email
from djoser.conf import settings as djoser_settings
from rest_framework import mixins, viewsets

from src.apps.accounts.serializers import (
    UserListSerializer,
    UserRetrieveSerializer,
    UserCreateSerializer,
)
from src.apps.accounts.services.db import get_all_users, get_user_by_username_or_none


class UserBaseViewSet(
    viewsets.GenericViewSet,
):
    queryset = get_all_users()
    serializer_class = UserListSerializer
    serializer_classes = {
        "list": UserListSerializer,
        "retrieve": UserRetrieveSerializer,
        "create": UserCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)


class UserViewSet(
    UserBaseViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = djoser_settings.PERMISSIONS.user_create
        return super().get_permissions()

    def perform_create(self, serializer, *args, **kwargs):
        user = serializer.save(*args, **kwargs)
        djoser_signals.user_registered.send(
            sender=self.__class__,
            user=user,
            request=self.request,
        )

        context = {"user": user}
        to = [get_user_email(user)]
        if djoser_settings.SEND_ACTIVATION_EMAIL:
            djoser_settings.EMAIL.activation(self.request, context).send(to)
        elif djoser_settings.SEND_CONFIRMATION_EMAIL:
            djoser_settings.EMAIL.confirmation(self.request, context).send(to)


class UserByUsernameViewSet(
    UserBaseViewSet,
    mixins.RetrieveModelMixin,
):
    lookup_field = "username"

    def get_object(self):
        username = self.kwargs.get(self.lookup_field)
        user = get_user_by_username_or_none(username=username)
        if not user:
            raise Http404

        return user
