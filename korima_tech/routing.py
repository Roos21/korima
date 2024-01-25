# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/chat/<str:user_1>/<str:user_2>/", consumers.ChatConsumer.as_asgi()),
    # Ajoutez d'autres configurations WebSocket au besoin...
]

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
