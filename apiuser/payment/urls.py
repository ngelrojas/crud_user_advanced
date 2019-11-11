from django.urls import path
from rest_framework.routers import DefaultRouter
from payment import views

urlpatterns = [
        path('payment', views.PaymentViewSet.as_view({
            'get': 'list',
            'post': 'create',
            'put': 'update'}),
            name='payment'),
        path('payment/<int:pk>', views.PaymentViewSet.as_view({
            'get': 'retrieve'}),
            name='details-payment'),
        path('payments', views.PaymentInCome.as_view({
            'get': 'list',
            'put': 'update'}),
            name='payments'),

]
