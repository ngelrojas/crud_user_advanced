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
    campaing_created = 1

    def list(self, request):
        queryset = Campaing.objects.filter(user=request.user)
        serializer = serializers.CampaingListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        try:
            queryset = Campaing.objects.filter(user=request.user)
            current_campaing = get_object_or_404(queryset, pk=pk)
            serializer = serializers.CampaingListSerializer(current_campaing)
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
                                                status_campaing=self.campaing_created
            )
            serializer = self.serializer_class(current_user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response({'data': 'campaing updated successufully.'}, status=status.HTTP_200_OK)
        except Campaing.DoesNotExist as err:
            return Response(
                    {'error': 'campaing not exists with that parameters'},
                    status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, pk=None):
        try:
            current_campaing = Campaing.objects.get(id=request.data.get('id'), status_campaing=2)
            current_campaing.is_enabled = False
            current_campaing.save()
            return Response({'data': 'campaing deleted successfully.'}, status=status.HTTP_200_OK)
        except Campaing.DoesNotExist as err:
            return Response({'error': 'something wrong.'}, status=status.HTTP_400_BAD_REQUEST)


class CampaingPublic(viewsets.ModelViewSet):
    """
    list:
        show all campaing with status public
    retrieve:
        display all campaings categories
    """
    serializer_class = serializers.CampaingSerializerPublic
    campaing_public = 3

    def get_queryset(self):
        queryset = Campaing.objects.filter(status_campaing=self.campaing_public)
        return queryset

    def retrieve(self, request, slug_title):
        try:
            queryset = Campaing.objects.filter(status_campaing=self.campaing_public)
            current_campaing = get_object_or_404(queryset, slug=slug_title)
            serializer = serializers.CampaingListSerializer(current_campaing)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        except Campaing.DoesNotExist as err:
            return Response(
                    {'error': 'something wrong.'},
                    status=status.HTTP_400_BAD_REQUEST
            )
