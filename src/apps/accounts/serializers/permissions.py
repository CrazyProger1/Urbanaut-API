from rest_framework import serializers

from src.apps.accounts.models import UserObjectPermission, TeamObjectPermission
from src.apps.accounts.serializers.users import UserListSerializer
from src.apps.accounts.serializers.teams import TeamListSerializer
from src.apps.accounts.services.db import (
    get_all_teams,
    get_all_users,
    reset_permissions,
)


class ActorsCreateSerializer(serializers.Serializer):
    users = serializers.PrimaryKeyRelatedField(
        queryset=get_all_users(),
        many=True,
        required=False,
        default=list,
    )
    teams = serializers.PrimaryKeyRelatedField(
        queryset=get_all_teams(),
        many=True,
        required=False,
        default=list,
    )


class ActorsRetrieveSerializer(serializers.Serializer):
    users = UserListSerializer(many=True)
    teams = TeamListSerializer(many=True)


class _PermissionsBaseSerializer(serializers.Serializer):
    def get_attribute(self, instance):
        return instance

    def to_representation(self, instance):
        user_perms = list(
            instance.permission.user_object_permissions.select_related("user").all()
        )
        team_perms = list(
            instance.permission.team_object_permissions.select_related("team").all()
        )
        return {
            "view": {
                "users": UserListSerializer(
                    [p.user for p in user_perms if p.is_visible], many=True
                ).data,
                "teams": TeamListSerializer(
                    [p.team for p in team_perms if p.is_visible], many=True
                ).data,
            },
            "edit": {
                "users": UserListSerializer(
                    [p.user for p in user_perms if p.is_editable], many=True
                ).data,
                "teams": TeamListSerializer(
                    [p.team for p in team_perms if p.is_editable], many=True
                ).data,
            },
        }


class PermissionsCreateSerializer(_PermissionsBaseSerializer):
    view = ActorsCreateSerializer(required=False)
    edit = ActorsCreateSerializer(required=False)


class PermissionsRetrieveSerializer(_PermissionsBaseSerializer):
    view = ActorsRetrieveSerializer()
    edit = ActorsRetrieveSerializer()


def _write_permissions(instance, permissions):
    view = permissions.get("view", {})
    edit = permissions.get("edit", {})
    view_users = set(view.get("users", []))
    view_teams = set(view.get("teams", []))
    edit_users = set(edit.get("users", []))
    edit_teams = set(edit.get("teams", []))

    UserObjectPermission.objects.bulk_create(
        [
            UserObjectPermission(
                permission=instance.permission,
                user=user,
                is_visible=user in view_users,
                is_editable=user in edit_users,
            )
            for user in view_users | edit_users
        ]
    )
    TeamObjectPermission.objects.bulk_create(
        [
            TeamObjectPermission(
                permission=instance.permission,
                team=team,
                is_visible=team in view_teams,
                is_editable=team in edit_teams,
            )
            for team in view_teams | edit_teams
        ]
    )


class PermissionsRetrieveSerializerMixin(serializers.ModelSerializer):
    permissions = PermissionsRetrieveSerializer()


class PermissionsCreateUpdateSerializerMixin(serializers.ModelSerializer):
    permissions = PermissionsCreateSerializer()

    def create(self, validated_data):
        permissions = validated_data.pop("permissions")
        instance = super().create(validated_data=validated_data)
        _write_permissions(instance=instance, permissions=permissions)
        return instance

    def update(self, instance, validated_data):
        permissions = validated_data.pop("permissions")
        instance = super().update(instance=instance, validated_data=validated_data)
        reset_permissions(obj=instance)
        _write_permissions(instance=instance, permissions=permissions)
        return instance
