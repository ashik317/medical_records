from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from notifications.models import Notification
from notifications.serializers import NotificationSerializer


class NotificationListAPIView(ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(
            user=self.request.user
        ).order_by('-created_at')

class NotificationDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "pk"

    def get_object(self):
        return Notification.objects.get(
            pk=self.kwargs['pk'],
            user=self.request.user
        )

    def perform_update(self, serializer):
        serializer.save(is_read=True)
