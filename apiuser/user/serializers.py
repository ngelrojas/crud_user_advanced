from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator
from rest_framework import serializers, fields
from rest_framework.generics import get_object_or_404
from django.utils.translation import gettext_lazy as _
from apiuser.celery import send_email_message
from core.tokens import encode_user_id, make_user_token,\
        decode_user_id
from core.models import CodeActivation, User


class UserSerializer(serializers.ModelSerializer):
    """serialzier for the users object"""
    last_name = serializers.CharField(required=True, max_length=255)
    dni = serializers.CharField(required=True, max_length=100)
    cellphone = serializers.CharField(required=True, max_length=255)
    address = serializers.CharField(max_length=300, default='')

    class Meta:
        model = get_user_model()
        fields = ('email',
                'password',
                'name',
                'last_name',
                'dni',
                'cellphone',
                'address',
                'photo',)
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validate_data):
        """create a new user with encrypted password and return it"""
        user_instance = get_user_model().objects.create_user(**validate_data)
        # send email confirmation
        uid = encode_user_id(user_instance.id)
        token = make_user_token(user_instance)
        email_context = {
                'fullname': '{}'.format(validate_data['name']),
                'domain': f'{settings.URL_PRODUCTION}/email-confirmation',
                'uid': uid,
                'token': token
        }
        tmp_name = 'emails/profile/activation-account-confirmation.html'
        send_email_message(
                subject='No reply',
                to=[validate_data['email'], ],
                body='',
                template_name=tmp_name,
                context=email_context,
        )
        CodeActivation.objects.create(
               code_token=uid+'_'+token,
               is_expired=False,
               user=user_instance
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


class ActivationAccountSerializer(serializers.Serializer):
    """serializer for the activation account user"""
    pass


class PasswordRecoverySerializer(serializers.Serializer):
    """serializer to recovery password"""
    email = fields.EmailField(validators=[EmailValidator(),])

    def create(self, validated_data):
        """send email to recovery password"""
        user = get_object_or_404(User, email=validated_data.get('email'))
        email_context = {
                'name': '{}'.format(user.name),
                'domain': f'{settings.URL_PRODUCTION}/recover-password',
                'uid': encode_user_id(user.id),
                'token': make_user_token(user),
        }
        send_email_message(
                subject='Cotizate - Password Recovery',
                to=[validated_data['email'], ],
                body='',
                template_name='emails/profile/recovery-password.html',
                context=email_context,
        )
        return validated_data


class PasswordRecoveryConfirmSerializer(serializers.Serializer):

    password = fields.CharField(
        style={'input_type': 'password'}, required=True,
    )
    password_confirmation = fields.CharField(
        style={'input_type': 'password'}, required=True,
    )


    def validate(self, attrs):
        """validation data password and password confirm"""
        if attrs.get('password') != attrs.get('password_confirmation'):
            raise serializers.ValidationError("Those passwords don't match")

        return attrs
