from rest_framework import generics, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from core.models import Reward, User
from reward import serializers


class RewardViewSet(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    """manage reward objects"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Reward.objects.all()
    serializer_class = serializers.RewardSerializer

    queryset = Reward.objects.all()

    def get(self, request, *args, **kwargs):
       list_reward = Reward.objects.filter(user_id=request.user.id)
       serializer = self.serializer_class(list_reward, many=True)
       return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
       # reward = Reward()
       # reward.user = request.user
       # reward.name = request.data.get('name')
       # reward.price = request.data.get('price')
       # reward.type_reward = request.data.get('type_reward')
       # reward.delivery_data = request.data.get('delivery_data')
       # reward.delivery_place = request.data.get('delivery_place')
       # reward.description = request.data.get('description')
       # reward.save()
       reward = self.serializer_class(data=request.data)
       reward.is_valid(raise_exception=True)
       return Response({'data': 'reward created successfully'}, status=status.HTTP_201_CREATED)
