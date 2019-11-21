from django.utils.timezone import now
from rest_framework import serializers
from core.models import Reward, User, Campaing


class RewardSerializer(serializers.ModelSerializer):
    """serializer for rewards object"""
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    type_reward = serializers.IntegerField(default=1)
    delivery_data = serializers.DateTimeField()
    delivery_place = serializers.CharField(max_length=400)

    class Meta:
        model = Reward
        fields = (
                'id',
                'title',
                'campaing',
                'price',
                'type_reward',
                'delivery_data',
                'delivery_place',
                'description',
        )
        read_only_fields = ('id',)

    def update(self, instance, validated_data):
        """update data reward """
        instance.name = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.type_reward = validated_data.get('type_reward', instance.type_reward)
        instance.delivery_data = validated_data.get('delivery_data', instance.delivery_data)
        instance.delivery_place = validated_data.get('delivery_place', instance.delivery_place)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
