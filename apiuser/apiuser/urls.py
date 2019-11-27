"""apiuser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='COTIZATE API')

urlpatterns = [
    path('api/v1/cotizate-doc/', schema_view),
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('user.urls')),
    path('api/v1/', include('tag.urls')),
    path('api/v1/', include('category.urls')),
    path('api/v1/', include('reward.urls')),
    path('api/v1/', include('campaing.urls')),
    path('api/v1/', include('payment.urls')),
    path('api/v1/', include('like.urls')),
    path('api/v1/', include('newscampaing.urls')),
    path('api/v1/', include('comment.urls')),
]
