from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import Payment, User, Campaing
from payment import serializers
from .tools import Tools


class PaymentViewSet(viewsets.ModelViewSet):
    """
    list:
        list all payments
    create:
        create a payments from current user
    retrieve:
        get a payment by id campaing
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Payment.objects.all()
    serializer_class = serializers.PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.all()
        return queryset

    def retrieve(self, request, pk):
        queryset = Payment.objects.all()
        current_payment = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(current_payment)
        return Response(
                {'data': serializer.data},
                status=status.HTTP_200_OK
        )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class PaymentInCome(viewsets.ModelViewSet):
    """
    list:
        show all payments
    update:
        update status payment by request from company payment
    """
    serializer_class = serializers.PayIncomeSerializer

    def get_queryset(self):
        queryset = Payment.objects.all()
        return queryset

    def update(self, request, pk=None):
        try:
            c_tools = Tools()
            current_user = c_tools.validate_user(request.data.get('user'))
            current_campaing = c_tools.validate_campaing(request.data.get('campaing'))
            current_payment = Payment.objects.get(user=current_user, campaing=current_campaing)
            serializer = self.serializer_class(current_payment, data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                        {'data': 'payment update successfully.'},
                        status=status.HTTP_200_OK
                )

            return Response(
                    {'error': 'something wrong.'},
                    status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as err:
            return Response({'error': f'{err}'})
