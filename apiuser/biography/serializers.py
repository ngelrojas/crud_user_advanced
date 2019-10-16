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
    is_representative = serializers.BooleanField(default=False)
    personal_website = serializers.CharField(max_length=255, default='')
    company_website = serializers.CharField(max_length=255, default='')
    company_name = serializers.CharField(max_length=255, default='')
    company_nit = serializers.CharField(max_length=255, default='')
    company_city = serializers.CharField(max_length=255, default='')
    company_phone = serializers.CharField(max_length=255, default='')
    company_address = serializers.CharField(max_length=300, default='')
    company_email = serializers.CharField(max_length=255, default='')
    company_logo = serializers.CharField(max_length=255, default='')
    company_description = serializers.CharField(max_length=255, default='')
    company_facebook = serializers.CharField(max_length=255, default='')
    company_twitter = serializers.CharField(max_length=255, default='')
    company_linkedin = serializers.CharField(max_length=255, default='')
    company_instagram = serializers.CharField(max_length=255, default='')

    class Meta:
        model = Biography
        fields = '__all__'
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
        instance.is_representative = validated_data.get('is_representative', instance.is_representative)
        instance.personal_website = validated_data.get('personal_website', instance.personal_website)
        instance.company_website = validated_data.get('company_website', instance.company_website)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.company_nit = validated_data.get('company_nit', instance.company_nit)
        instance.company_city = validated_data.get('company_city', instance.company_city)
        instance.company_phone = validated_data.get('company_phone', instance.company_phone)
        instance.company_address = validated_data.get('company_address', instance.company_address)
        instance.company_email = validated_data.get('company_email', instance.company_email)
        instance.company_logo = validated_data.get('company_logo', instance.company_logo)
        instance.company_description = validated_data.get('compnay_description', instance.company_description)
        instance.company_facebook = validated_data.get('company_facebook', instance.company_facebook)
        instance.company_twitter = validated_data.get('company_twitter', instance.company_twitter)
        instance.company_linkedin = validated_data.get('company_linkedin', instance.company_linkedin)
        instance.company_instagram = validated_data.get('company_instagram', instance.company_instagram)
        instance.is_complete = True
        instance.save()

        return instance
