# utils.py
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

def push_notifications(user_id, data):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"notifications_{user_id}",
        {
            "type": "send_notification",
            "message": json.dumps(data)
        }
    )