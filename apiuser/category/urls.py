from django.urls import path
from rest_framework.routers import DefaultRouter
from category import views

router = DefaultRouter()
router.register('category', views.CategoryViewSet)

urlpatterns = [
        path('category', views.CategoryViewSet.as_view({
            'get': 'list',
            'post': 'create',
            'put': 'update',
            'delete': 'destroy'}),
            name='category'
        ),
        path('category/<int:pk>', views.CategoryViewSet.as_view({
            'get': 'retrieve'}),
            name='detail-category'
        ),
]
