from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tag import views


router = DefaultRouter()
router.register('tag', views.TagViewSet)

urlpatterns = [
        path('tag', views.TagViewSet.as_view({
                                            'get': 'list',
                                            'post': 'create',
                                            'delete': 'destroy'}),
                                            name='tag')
]
