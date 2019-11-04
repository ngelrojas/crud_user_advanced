from django.urls import path
from rest_framework.routers import DefaultRouter
from campaing import views

urlpatterns = [
        path('campaing', views.CampaingViewSet.as_view({
                                                        'get': 'list',
                                                        'retrieve': 'retrieve',
                                                        'post': 'create',
                                                        'put': 'update',
                                                        'delete': 'destroy'}),
                                                        name='campaing'
        ),
        path('campaings', views.CampaingPublic.as_view({'get': 'list'}), name='campaings')
]
