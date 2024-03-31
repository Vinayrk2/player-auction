from django.urls import path
from .consumers import MyConsumer

websocket_urlpatterns = [
    path('ws/<str:dashboard>', MyConsumer.as_asgi()),
]