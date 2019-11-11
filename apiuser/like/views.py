from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import User, Like
from like import serializers


class LikeViewSet(viewsets.ModelViewSet):
    """
    list:
        show all likes
    create:
        create likes from current user
    update:
        updated likes
    """
    serializer_class = serializers.LikeSerializer

    def get_queryset(self):
        queryset = Like.objects.all()
        return queryset

    def retrieve(self, request, pk):
        queryset = Like.objects.get(campaing=pk)
        serializer = self.serializer_class(queryset)
        return Response({
            'data': serializer.data},
            status=status.HTTP_200_OK
        )

    def perform_create(self, serializer):
        return serializer.save()

    def update(self, request, pk=None):
        pass
