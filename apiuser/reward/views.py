from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from core.models import Reward, User
from reward import serializers


class RewardViewSet(viewsets.ModelViewSet):
    """manage reward objects"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Reward.objects.all()
    serializer_class = serializers.RewardSerializer

    def get_queryset(self):
        queryset = Reward.objects.filter(id=self.request.data.get('id'))
        return queryset

    def create(self, request, *args, **kwargs):
        """create a new reward"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'error': 'something wrong'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """update reward from current user"""
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'data': "reward updated successufully."}, status=status.HTTP_200_OK)
        except Reward.DoesNotExist as err:
            return Response({'error': "something wrong in update reward"},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """delete current reward"""
        try:
            current_reward = Reward.objects.get(id=request.data.get('id'))
            current_reward.delete()
            return Response({'data': 'reward deleted successufully'}, status=status.HTTP_200_OK)
        except Reward.DoesNotExist as err:
            return Response({'error': 'something wrong.'}, status=status.HTTP_400_BAD_REQUEST)
