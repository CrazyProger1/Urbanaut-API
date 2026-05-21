from rest_framework import serializers

from src.apps.accounts.models import UserObjectPermission, TeamObjectPermission
from src.apps.accounts.services.db import get_all_teams, get_all_users, reset_permissions


class ActorsSerializer(serializers.Serializer):
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


class PermissionsSerializer(serializers.Serializer):
    view = ActorsSerializer(required=False)
    edit = ActorsSerializer(required=False)

    def get_attribute(self, instance):
        return instance

    def to_representation(self, instance):
        user_perms = list(instance.permission.user_object_permissions.all())
        team_perms = list(instance.permission.team_object_permissions.all())
        return {
            "view": {
                "users": [p.user_id for p in user_perms if p.is_visible],
                "teams": [p.team_id for p in team_perms if p.is_visible],
            },
            "edit": {
                "users": [p.user_id for p in user_perms if p.is_editable],
                "teams": [p.team_id for p in team_perms if p.is_editable],
            },
        }


class PermissionsSerializerMixin(serializers.ModelSerializer):
    permissions = PermissionsSerializer()

    def create(self, validated_data):
        permissions = validated_data.pop("permissions")
        instance = super().create(validated_data=validated_data)
        self._write_permissions(instance=instance, permissions=permissions)
        return instance

    def update(self, instance, validated_data):
        permissions = validated_data.pop("permissions")
        instance = super().update(instance=instance, validated_data=validated_data)
        reset_permissions(obj=instance)
        self._write_permissions(instance=instance, permissions=permissions)
        return instance

    @staticmethod
    def _write_permissions(instance, permissions):
        view = permissions.get("view", {})
        edit = permissions.get("edit", {})
        view_users = set(view.get("users", []))
        view_teams = set(view.get("teams", []))
        edit_users = set(edit.get("users", []))
        edit_teams = set(edit.get("teams", []))

        UserObjectPermission.objects.bulk_create([
            UserObjectPermission(
                permission=instance.permission,
                user=user,
                is_visible=user in view_users,
                is_editable=user in edit_users,
            )
            for user in view_users | edit_users
        ])
        TeamObjectPermission.objects.bulk_create([
            TeamObjectPermission(
                permission=instance.permission,
                team=team,
                is_visible=team in view_teams,
                is_editable=team in edit_teams,
            )
            for team in view_teams | edit_teams
        ])
