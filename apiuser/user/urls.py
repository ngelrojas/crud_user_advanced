from django.urls import path, re_path
from user import views
from biography import views as view_bio


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    re_path(
        r'^activate/(?P<uid>[0-9A-Za-z_\-]+)/' +
        '(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.ActivationAccount.as_view(), name='activate'),
    path('recovery-password/',
        views.PasswordRecovery.as_view(),
        name='recovery-password'),
    path('recovery-password-confirm/',
        views.PasswordRecoveryConfirm.as_view(),
        name='recovery-password-confirm'),
    path('biography/', view_bio.BiographyView.as_view({
                                                        'get': 'retrieve',
                                                        'put': 'update'}),
                                                        name='biography')
]
