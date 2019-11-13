from django.utils.timezone import now
from rest_framework import serializers
from core.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """serializers for likes"""
    class Meta:
        model = Like
        fields = (
                'id',
                'liked',
                'user',
                'campaing',
        )
    read_only_fields = ('id',)
