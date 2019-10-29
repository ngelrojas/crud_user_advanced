from django.urls import path
from rest_framework.routers import  DefaultRouter
from reward import views

urlpatterns = [
        path('reward', views.RewardViewSet.as_view(), name='reward')
]
