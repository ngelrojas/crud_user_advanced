from django.urls import path
from like import views

urlpatterns = [
        path('like', views.LikeViewSet.as_view({
            'get': 'list',
            'post': 'create',
            'put': 'update'}),
            name='like'),
        path('like/<int:pk>', views.LikeViewSet.as_view({
            'get': 'retrieve'}),
            name='details-like'),
]
