from rest_framework import serializers
from core.models import CategoryCampaing, Campaing


class CategoryCampaingSerializer(serializers.ModelSerializer):
    """serializer for category objects"""
    campaing = serializers.PrimaryKeyRelatedField(
            many=True,
            queryset=Campaing.objects.all()
    )

    class Meta:
        model = CategoryCampaing
        fields = ('id', 'name', 'campaing',)
        read_only_fields = ('id',)
