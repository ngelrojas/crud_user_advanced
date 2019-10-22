from django.urls import path
from rest_framework.routers import DefaultRouter

from tag import views

urlpatterns = [
        path('tag', views.TagViewSet.as_view({
                                            'get': 'list',
                                            'post': 'create',
                                            'delete': 'destroy'}),
                                            name='tag')
]
