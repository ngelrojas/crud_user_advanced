from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import Campaing, User, TagCampaing
from campaing import serializers


class CampaingViewSet(viewsets.ModelViewSet):
    """
    list:
        get all campaing from current user
    retrieve:
        get a detail campaing from current user
    create:
        create campaing from current user
    update:
        update campaing from current user and current campaing
    destroy:
        delete current campaing
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Campaing.objects.all()
    serializer_class = serializers.CampaingSerializer

    def list(self, request):
        queryset = Campaing.objects.filter(user=request.user, is_enabled=True)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        try:
            queryset = Campaing.objects.all()
            current_campaing = get_object_or_404(queryset, pk=pk)
            serializer = self.serializer_class(current_campaing)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        except Campaing.DoesNotExist as err:
            return Response(
                    {'error': 'something wrong.'},
                    status=status.HTTP_400_BAD_REQUEST
            )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def update(self, request, pk=None):
        try:
            current_user = Campaing.objects.get(user=request.user,
                                                id=request.data.get('id'),
                                                is_enabled=True
            )
            serializer = self.serializer_class(current_user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response({'data': 'campaing updated successufully.'}, status=status.HTTP_200_OK)
        except Campaing.DoesNotExist as err:
            return Response({'error': 'something wrong.'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            current_campaing = Campaing.objects.get(id=request.data.get('id'), is_enabled=True)
            current_campaing.is_enabled = False
            current_campaing.save()
            return Response({'data': 'campaing deleted successfully.'}, status=status.HTTP_200_OK)
        except Campaing.DoesNotExist as err:
            return Response({'error': 'something wrong.'}, status=status.HTTP_400_BAD_REQUEST)


class CampaingPublic(viewsets.ModelViewSet):
    """
    list:
        show all campaing
    """
    serializer_class = serializers.CampaingSerializerPublic

    def get_queryset(self):
        queryset = Campaing.objects.filter(is_enabled=True)
        return queryset
