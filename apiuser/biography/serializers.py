from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, fields
from core.models import User, Biography


class BiographySerializer(serializers.ModelSerializer):
    """serializer fro biography objects"""

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
