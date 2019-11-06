from django.utils.timezone import now
from rest_framework import serializers
from core.models import Payment, Campaing, User


class PaymentSerializer(serializers.ModelSerializer):
    """serializer for payments"""

    class Meta:
        model = Payment
        fields = (
                'id',
                'name',
                'campaing',
                'user',
                'type_payment',
                'budget_partial',
                'created_at',
        )
        read_only_fields = ('id',)

