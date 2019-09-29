from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from apiuser.celery import send_email_message


class UserSerializer(serializers.ModelSerializer):
    """serialzier for the users object"""
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validate_data):
        """create a new user with encrypted password and return it"""
        user_instance = get_user_model().objects.create(**validate_data)
        # send email confirmation
        email_context = {
                'fullname': '{}'.format(validate_data['name']),
                'domain': f'{settings.URL_PRODUCTION}/email-confirmation',
                'uid': 'asdf2123',
                'token': 'token-id'
        }
        tmp_name = 'emails/profile/activation-account-confirmation.html'
        send_email_message(
                subject='No reply',
                to=[validate_data['email'], ],
                body='',
                template_name=tmp_name,
                context=email_context,
        )

        return user_instance

    def update(self, instance, validated_data):
        """update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
            style={'input_type': 'password'},
            trim_whitespace=False
    )

    def validate(self, attrs):
        """validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
                request=self.context.get('request'),
                username=email,
                password=password
        )
        if not user:
            msg = _('unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
