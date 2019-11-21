from django.urls import path
from rest_framework.routers import  DefaultRouter
from reward import views

urlpatterns = [
        path('reward', views.RewardViewSet.as_view({
            'post': 'create',
            'put': 'update',
            'delete': 'destroy'}),
            name='reward'),
        path('reward/<int:pk>', views.RewardViewSet.as_view({
            'get': 'list'}),
            name='display-rewards'
        ),
        path('rewards/<int:pk>', views.RewardPublic.as_view({
            'get': 'list'}),
            name='rewards'
        ),
]
