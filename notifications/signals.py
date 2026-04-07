from django.contrib.auth import user_logged_in
from django.dispatch import receiver

from .models import Notification
from .utils import push_notifications

@receiver(user_logged_in)
def notify_on_login(sender, request, user, **kwargs):
    notif = Notification.objects.create(
        user=user,
        title="Login Alert",
        message="You logged in successfully"
    )
    # Push via WebSocket
    push_notifications(user.id, {
        "id": notif.id,
        "title": notif.title,
        "message": notif.message,
        "created_at": notif.created_at.isoformat()
    })