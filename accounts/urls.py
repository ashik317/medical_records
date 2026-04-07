from django.urls import path
from accounts.views import UserRegisterListApiView, UserListApiView, UserDetailApiView

urlpatterns = [
    path(
        'register/',
        UserRegisterListApiView.as_view(),
        name='register'
    ),
    path(
        'user/',
        UserListApiView.as_view(),
        name='register'
    ),
    path(
        'user/<uuid:alias>/',
        UserDetailApiView.as_view(),
    )
]
