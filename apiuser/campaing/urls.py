from django.urls import path
from rest_framework.routers import DefaultRouter
from campaing import views

urlpatterns = [
        path('campaing', views.CampaingViewSet.as_view({
                                                        'get': 'list',
                                                        'post': 'create',
                                                        'put': 'update'}), name='campaing')
]
