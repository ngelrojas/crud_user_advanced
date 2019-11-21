from django.utils.timezone import now
from rest_framework import serializers
from core.models import Campaing, User, TagCampaing


class CampaingSerializer(serializers.ModelSerializer):
    """serializer for campaing"""
    title = serializers.CharField(max_length=255)
    slug = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    budget = serializers.FloatField(max_value=None, min_value=None)
    qty_days = serializers.IntegerField(default=0)
    facebook = serializers.CharField(max_length=255)
    twitter = serializers.CharField(max_length=255)
    linkedin = serializers.CharField(max_length=255)
    instagram = serializers.CharField(max_length=255)
    website = serializers.CharField(max_length=255)
    video = serializers.CharField(max_length=255)
    excerpt = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=None)
    updated_at = serializers.DateTimeField(default=now)
    tags = serializers.PrimaryKeyRelatedField(
            many=True,
            queryset=TagCampaing.objects.all()
    )

    class Meta:
        model = Campaing
        fields = (
                'id',
                'title',
                'slug',
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

        read_only_fields = ('id',)


class TagPublicSerializer(serializers.ModelSerializer):
    """serilizer public tags"""

    class Meta:
        model = TagCampaing
        fields = ('id', 'name',)


class CampaingSerializerPublic(serializers.ModelSerializer):
    """campaing serializer public"""
    tags = TagPublicSerializer(many=True, read_only=True)

    class Meta:
        model = Campaing
        fields = (
                'title',
                'slug',
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
                'tags',
        )

        read_only_fields = ('id',)
