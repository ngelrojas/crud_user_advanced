from django.urls import path
from rest_framework.routers import DefaultRouter
from payment import views

urlpatterns = [
        path('payment', views.PaymentViewSet.as_view({
            'get': 'list'}),
            name='payment'),
]
