from django.urls import path
from rest_framework.routers import DefaultRouter

from tag import views

urlpatterns = [
        path('tag', views.TagViewSet.as_view({
            'get': 'list',
            'post': 'create',
            'delete': 'destroy'}),
            name='tag'
        ),
        path('tag/<int:pk>', views.TagViewSet.as_view({
            'get': 'retrieve'}),
            name='detail-tag'
        ),
        path('tags', views.TagPublic.as_view({
            'get': 'list'}),
            name='tags'
        ),
        path('tags/<int:pk>', views.TagPublic.as_view({
            'get': 'retrieve'}),
            name='retrieve-tags'
        ),
]
