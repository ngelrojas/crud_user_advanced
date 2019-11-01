from django.utils.timezone import now
from rest_framework import serializers
from core.models import Campaing, User


class CampaingSerializer(serializers.ModelSerializer):
    """serializer for campaing"""
    title = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    category_id = serializers.IntegerField(default=0)
    tag_id = serializers.IntegerField(default=0)
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
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Campaing
        fields = (
                'id',
                'title',
                'city',
                'category_id',
                'tag_id',
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
                'updated_at',)

        read_only_fields = ('id',)

    def create(self, validated_data):
        return Campaing.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """update data campaing"""
        instance.title = validated_data.get('title', instance.title)
        instance.city = validated_data.get('city', instance.city)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.tag_id = validated_data.get('tag_id', instance.tag_id)
        instance.budget = validated_data.get('budget', instance.budget)
        instance.qty_days = validated_data.get('qty_days', instance.qty_days)
        instance.facebook = validated_data.get('facebook', instance.facebook)
        instance.twitter = validated_data.get('twitter', instance.twitter)
        instance.linkedin = validated_data.get('linkedin', instance.linkedin)
        instance.instagram = validated_data.get('instagram', instance.instagram)
        instance.website = validated_data.get('website', instance.website)
        instance.video = validated_data.get('video', instance.video)
        instance.excerpt = validated_data.get('excerpt', instance.excerpt)
        instance.description = validated_data.get('description', instance.description)
        instance.updated_at = now
        instance.save()
        return instance
