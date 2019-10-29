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
        try:
            current_user = self.context['request'].user
            reward = Reward.objects.create(user=current_user, **validated_data)
            return reward
        except Exception as err:
            return f'err'
