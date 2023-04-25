from django.urls import path
from .views import RoomChat, RoomCreate

urlpatterns = [
    path("rooms/<int:pk>/", RoomChat.as_view(), name="room-chat"),
    path("rooms/create/", RoomCreate.as_view(), name="create-room"),
]
