from user.serializers import UserSerializer
from django.contrib.auth.models import Group, Permission
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, viewsets
from django.contrib.auth import get_user_model
from .serializers import GroupsSerializer, PermissionSerializer
import json


class UserGroupsView(viewsets.ModelViewSet):
    serializer_class = GroupsSerializer
    queryset = Group.objects.all()
    permission_classes = (permissions.AllowAny,)

    @action(methods=['post'], detail=True)
    def add(self, request, pk):
        groups = json.loads(request.data['groups'])
        for i in groups:
            g = Group.objects.get(id=i)
            try:
                g.user_set.add(pk)
            except:
                next

        return Response(json.dumps(groups))


class UserPermissionsView(viewsets.ModelViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
    permission_classes = (permissions.AllowAny,)

    @action(methods=['post'], detail=True)
    def add(self, request, pk):
        permissions = json.loads(request.data['user_permissions'])
        user = get_user_model().objects.get(id=pk)
        try:
            user.user_permissions.set(permissions)
        except:
            print("SQLite3")
            user.user_permissions.clear()
            for i in permissions:
                p = Permission.objects.get(id=i)
                try:
                    user.user_permissions.add(p)
                except:
                    next
        return Response(json.dumps(permissions))
