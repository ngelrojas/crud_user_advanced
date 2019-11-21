from rest_framework import serializers
from core.models import CategoryCampaing, Campaing
from core.models import TagCampaing


class TagPublicSerializer(serializers.ModelSerializer):
    """serializer tag public"""
    class Meta:
        model = TagCampaing
        fields = ('id', 'name')


class CampaingPublicSerializer(serializers.ModelSerializer):
    """serializer campaing public"""
    tags = TagPublicSerializer(many=True, read_only=True)

    class Meta:
        model = Campaing
        fields = (
                'id',
                'title',
                'city',
                'budget',
                'qty_days',
                'facebook',
                'twitter',
                'linkedin',
                'instagram',
                'website',
                'video',
                'excerpt',
                'description',
                'created_at',
                'updated_at',
                'is_enabled',
                'tags',
        )


class CategoryCampaingSerializer(serializers.ModelSerializer):
    """serializer for category objects"""
    campaing = serializers.PrimaryKeyRelatedField(
            many=True,
            queryset=Campaing.objects.all()
    )

    class Meta:
        depth = 1
        model = CategoryCampaing
        fields = ('id', 'name', 'campaing',)
        read_only_fields = ('id',)


class CategoryPublicSerializer(serializers.ModelSerializer):
    """serializer category public"""
    campaing = CampaingPublicSerializer(many=True, read_only=True)

    class Meta:
        depth = 1
        model = CategoryCampaing
        fields = ('id', 'name', 'campaing',)
