from django.urls import path
from .views import NotificationListAPIView, NotificationDetailAPIView

urlpatterns = [
    path("notify/",
         NotificationListAPIView.as_view(),
         name="notifications-list"
    ),
    path("notify/<int:pk>/read/",
         NotificationDetailAPIView.as_view(),
         name="notifications-mark-read"
    ),
]