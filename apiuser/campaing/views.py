from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import Campaing, User
from campaing import serializers


class CampaingViewSet(viewsets.ModelViewSet):
    """
    list:
        get all campaing from current user
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

    def get_queryset(self):
        queryset = Campaing.objects.filter(user=self.request.user, is_enabled=True)
        return queryset

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def update(self, request, pk=None):
        try:
            current_user = Campaing.objects.get(user=request.user,
                                                id=request.data.get('id'),
                                                is_enabled=True
            )
            serializer = self.serializer_class(current_user, data=request.data)
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
