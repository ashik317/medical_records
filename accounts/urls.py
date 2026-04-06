from django.urls import path
from accounts.views import UserRegisterListApiViews

urlpatterns = [
    path(
        'register/',
        UserRegisterListApiViews.as_view(),
        name='register'
    )
]
