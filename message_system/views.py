from django.db.models import F
from rest_framework import permissions, viewsets, pagination
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from message_system.permissions import IsOwnerOrReadOnly

from .models import UserGroup, Message, MessageRecipient
from .serializers import UserGroupSeializer, MessageSeializer, MessageRecipientSeializer, MessageRecipientViewSeializer, MessageGroupRecipientsSeializer


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class UserGroupView(viewsets.ModelViewSet):
    serializer_class = UserGroupSeializer
    pagination_class = StandardResultsSetPagination
    queryset = UserGroup.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (permissions.IsAuthenticated,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated,)
        return super(UserGroupView, self).get_permissions()


class MessageView(viewsets.ModelViewSet):
    serializer_class = MessageSeializer
    pagination_class = LargeResultsSetPagination
    queryset = Message.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (permissions.IsAuthenticated,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated,)
        if self.request.method == 'DELETE':
            self.permission_classes = (
                permissions.IsAuthenticated,)
        return super(MessageView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        queryset = Message.objects.all().filter(group_message_id=pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = MessageSeializer(queryset, many=True)
        return Response(serializer.data)


class MessageRecipientView(viewsets.ModelViewSet):
    serializer_class = MessageRecipientSeializer
    pagination_class = LargeResultsSetPagination
    queryset = MessageRecipient.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (permissions.IsAuthenticated,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated,)
        return super(MessageRecipientView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        queryset = MessageRecipient.objects.all().filter(recipient=pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = MessageRecipientViewSeializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = MessageRecipientViewSeializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def group(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        # .distinct('recipient')
        queryset = MessageRecipient.objects.all().filter(
            recipient_group_id=pk).all()
        # .values('recipient_id').distinct()

        # newlist = []
        # for i in queryset:
        #     print(i)
        #     if i.recipient_id not in newlist:
        #         newlist.append(i.recipient_id)

        # print(newlist)

        serializer = MessageGroupRecipientsSeializer(queryset, many=True)
        return Response(serializer.data)
