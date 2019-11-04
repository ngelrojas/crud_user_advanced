from rest_framework import serializers
from core.models import TagCampaing


class TagCampaingSerializer(serializers.ModelSerializer):
    """serializer for tag objects"""

    class Meta:
        model = TagCampaing
        fields = ('id', 'name',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        return TagCampaing.objects.create(**validated_data)
