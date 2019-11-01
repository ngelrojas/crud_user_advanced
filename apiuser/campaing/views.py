from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import Campaing, User
from campaing import serializers


class CampaingViewSet(viewsets.ModelViewSet):
    """manage campaing objects"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Campaing.objects.all()
    serializer_class = serializers.CampaingSerializer

    def get_queryset(self):
        queryset = Campaing.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        """create campaing from current user"""
        return serializer.save(user=self.request.user)

    def update(self, request, pk=None):
        """update campaing from current user"""
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'data': 'campaing updated successufully.'}, status=status.HTTP_200_OK)
        except Campaing.DoesNotExist as err:
            return Response({'error': 'something wrong.'}, status=status.HTTP_400_BAD_REQUEST)
