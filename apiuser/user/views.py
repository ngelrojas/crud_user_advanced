from rest_framework import generics, authentication,\
        permissions, status, mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from user.serializers import UserSerializer, AuthTokenSerializer, ActivationAccountSerializer
from user.serializers import PasswordRecoverySerializer, PasswordRecoveryConfirmSerializer
from core.models import CodeActivation, User
from core.tokens import decode_user_id


class CreateUserView(generics.CreateAPIView):
    """create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    render_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """retrieve and return authentication user"""
        return self.request.user


class ActivationAccount(generics.UpdateAPIView):
    """
    update:
        update a current token to activate to current user
    """
    serializer_class = ActivationAccountSerializer

    def update(self, request, *args, **kwargs):
        """
        update token
        """
        uid = self.kwargs.get('uid')
        token = self.kwargs.get('token')
        url_token = uid+'_'+token

        try:
            token = CodeActivation.objects.get(code_token=url_token)
        except CodeActivation.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if token.is_expired:
            return Response(
                    data={'detail': 'Expired Token'},
                    status=status.HTTP_400_BAD_REQUEST,
            )

        decode_url_id = decode_user_id(uid)

        user = get_object_or_404(User, id=decode_url_id)
        user.is_active = True
        user.save()

        token.is_expired = True
        token.save()

        return Response(status=status.HTTP_200_OK)


class PasswordRecovery(generics.CreateAPIView):
    """create and confirm password recovery"""
    serializer_class = PasswordRecoverySerializer
    render_classes = api_settings.DEFAULT_RENDERER_CLASSES


class PasswordRecoveryConfirm(generics.RetrieveUpdateAPIView):
    """confirm password recovery"""
    serializer_class = PasswordRecoveryConfirmSerializer
    render_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def get_queryset(self):
        """retrieve and return authentication user"""
        return

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
