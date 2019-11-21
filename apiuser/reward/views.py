from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import Reward
from reward import serializers


class RewardViewSet(viewsets.ModelViewSet):
    """
    list:
        list all rewards
    create:
        create a reward from related campaing
    update:
        update a reward
    delete:
        delete a reward
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Reward.objects.all()
    serializer_class = serializers.RewardSerializer

    def get_queryset(self):
        queryset = Reward.objects.filter(
                campaing=self.kwargs['pk']
        )
        return queryset

    def perform_create(self, serializer):
        return serializer.save()

    def update(self, request, pk=None):
        try:
            current_rewards = Reward.objects.get(
                    campaing=request.data.get('campaing')
            )
            serializer = self.serializer_class(
                    current_rewards,
                    data=request.data
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                        {'data': "reward updated successufully."},
                        status=status.HTTP_200_OK
                )
        except Reward.DoesNotExist as err:
            return Response(
                    {'error': "something wrong in update reward"},
                    status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, pk=None):
        try:
            if not request.data.get('id'):
                return Response(
                        {'error': 'ID is required.'},
                        status=status.HTTP_400_BAD_REQUEST
                )

            current_reward = Reward.objects.get(id=request.data.get('id'))
            current_reward.delete()
            return Response(
                    {'data': 'reward deleted successufully'},
                    status=status.HTTP_200_OK
            )
        except Reward.DoesNotExist as err:
            return Response(
                    {'error': 'something wrong.'},
                    status=status.HTTP_400_BAD_REQUEST
            )


class RewardPublic(viewsets.ModelViewSet):
    """
    list:
        display all rewards public
    """
    serializer_class = serializers.RewardSerializer

    def get_queryset(self):
        queryset = Reward.objects.filter(
                campaing=self.kwargs['pk']
        )
        return queryset
