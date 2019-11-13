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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer

    def get_queryset(self):
        queryset = Like.objects.all()
        return queryset

    def retrieve(self, request, pk):
        queryset = Like.objects.get(campaing=pk, liked=True)
        serializer = self.serializer_class(queryset)
        return Response({
            'data': serializer.data},
            status=status.HTTP_200_OK
        )

        def perform_create(self, serializer):
            return serializer.save(owner=self.request.user)

    def update(self, request, pk=None):
        try:
            current_like = Like.objects.get(id=request.data.get('id'))
            serializer = self.serializer_class(current_like, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                        {'data': 'likes updated'},
                        status=status.HTTP_200_OK
                )
        except Like.DoesNotExist as err:
            return Response(
                    {'error': 'something wrong.'},
                    status=status.HTTP_404_NOT_FOUND
            )
