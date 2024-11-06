"""
Views for the core API.
"""
from rest_framework import viewsets
from core.models import UserGroups, Permissions
from core.serializers import UserGroupsSerializer, PermissionsSerializer

from rest_framework.settings import api_settings
from rest_framework import generics


class CreateUserGroupsViewSets(viewsets.ModelViewSet):
    """ViewSet for the UserGroups model."""
    queryset = UserGroups.objects.all()
    serializer_class = UserGroupsSerializer

class PermissionsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing permissions instances.
    """
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer