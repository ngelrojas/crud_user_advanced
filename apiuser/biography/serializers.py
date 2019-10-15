from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, fields
from rest_framework.generics import get_object_or_404
from core.models import User, Biography


class BiographySerializer(serializers.ModelSerializer):
    """serializer fro biography objects"""
    terms_cond = serializers.BooleanField(default=True)
    address_2 = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(required=True, max_length=100)
    email_2 = serializers.CharField(max_length=255)
    b_facebook = serializers.CharField(max_length=255)
    b_twitter = serializers.CharField(max_length=255)
    b_linkedin = serializers.CharField(max_length=255)
    b_instagram = serializers.CharField(max_length=255)
    is_complete = serializers.BooleanField(default=False)

    class Meta:
        model = Biography
        fields = ('user',
                'terms_cond',
                'updated_at',
                'address_2',
                'phone_number',
                'email_2',
                'b_facebook',
                'b_twitter',
                'b_linkedin',
                'b_instagram',
                'is_complete',
        )
        read_only_fields = ('user',)

    def create(self, validate_data):
        return Biography.objects.create(**validate_data)

    def update(self, instance, validated_data):
        """update data biography current user"""
        instance.address_2 = validated_data.get('address_2', instance.address_2)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email_2 = validated_data.get('email_2', instance.email_2)
        instance.b_facebook = validated_data.get('b_facebook', instance.b_facebook)
        instance.b_twitter = validated_data.get('b_twitter', instance.b_twitter)
        instance.b_linkedin = validated_data.get('b_linkedin', instance.b_linkedin)
        instance.b_instagram = validated_data.get('b_instagram', instance.b_instagram)
        instance.is_complete = True
        instance.save()

        return instance
