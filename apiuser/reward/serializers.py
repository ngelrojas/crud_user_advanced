from django.utils.timezone import now
from rest_framework import serializers
from core.models import Reward


class RewardSerializer(serializers.ModelSerializer):
    """serializer for rewards object"""
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    type_reward = serializers.IntegerField(default=1)
    delivery_data = serializers.DateTimeField()
    delivery_place = serializers.CharField(max_length=400)
    user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user_reward = serializers.IntegerField(default=0)

    class Meta:
        model = Reward
        fields = (
                'user',
                'name',
                'price',
                'type_reward',
                'delivery_data',
                'delivery_place',
                'description',
                'user_reward',
        )
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Reward.objects.create(**validated_data)
