from rest_framework.response import Response
from followers.permissions import IsAccountOwner
from messagers.serializers import MessageSerializer
from .serializers import RoomSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Room
from .serializers import RoomSerializer
from rest_framework import generics
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class RoomChat(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def post(self, request, pk):
        room = self.get_object()

        # Join the room's channel group
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_add)(
            f"room_{room.id}", self.request.user.channel_name
        )

        # Create a new message in the room
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(room=room, author=request.user)

        # Return the list of messages in the room
        messages = MessageSerializer(room.messages.all(), many=True).data
        data = {"room": RoomSerializer(room).data, "messages": messages}
        return Response(data)



class RoomCreate(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(creator_id=self.request.user.id)
