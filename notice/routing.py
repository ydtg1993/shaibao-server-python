from django.urls import path
from .consumers import ChatConsumer
# from .sync_consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/three/<str:user_token>', ChatConsumer),
    # path('ws/chat/<str:room_name>/', ChatConsumer),
]
