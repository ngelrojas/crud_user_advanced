from django.urls import path
from rest_framework.routers import DefaultRouter
from campaing import views

urlpatterns = [
        path('campaing', views.CampaingViewSet.as_view({
            'get': 'list',
            'post': 'create',
            'put': 'update',
            'delete': 'destroy'}),
            name='campaing'
        ),
        path('campaing/<int:pk>', views.CampaingViewSet.as_view({
            'get': 'retrieve'}),
            name='detail-campaing'
        ),
        path('campaings', views.CampaingPublic.as_view({
            'get': 'list'}),
            name='campaings'
        ),
        path('campaings/<slug:slug_title>', views.CampaingPublic.as_view({
            'get': 'retrieve'}),
            name='detail-campaings'
        ),
]
