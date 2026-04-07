# asgi.py
import os

# ✅ This MUST be first — before any other Django/channels imports
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_records.settings')

from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()  # ✅ Initialize Django second

# Only import these AFTER Django is initialized
from channels.routing import ProtocolTypeRouter, URLRouter
from notifications.middleware import JWTAuthMiddleware
import notifications.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": JWTAuthMiddleware(
        URLRouter(notifications.routing.websocket_urlpatterns)
    ),
})