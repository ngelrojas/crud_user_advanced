from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import Payment
from payment import serializers


class PaymentViewSet(viewsets.ModelViewSet):
    """
    list:
        list all payments
    create:
        create a payments from current user
    retrieve:
        get a payment by id campaing
    update:
        update payment from current user
    delete:
        delete payment
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Payment.objects.all()
    serializer_class = serializers.PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.all()
        return queryset
