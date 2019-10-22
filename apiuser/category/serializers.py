from rest_framework import serializers
from core.models import CategoryCampaing


class CategoryCampaingSerializer(serializers.ModelSerializer):
    """serializer for category objects"""

    class Meta:
        model = CategoryCampaing
        fields = ('id', 'name')
        read_only_fields = ('id',)

    def create(self, validated_data):
        return CategoryCampaing.objects.create(**validated_data)
