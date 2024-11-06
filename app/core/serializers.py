
from core.models import UserGroups, Permissions

from rest_framework import serializers

class UserGroupsSerializer(serializers.ModelSerializer):
    """Serializer for the UserGroups model."""

    class Meta:
        model = UserGroups
        fields = ['group_id', 'group_name', 'group_description', 'created_at', 'permission']
        read_only_fields = ['group_id', 'created_at']

class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = ['permission_id', 'permission_name', 'description']
        read_only_fields = ['permission_id']