import pdb
from django.shortcuts import get_object_or_404
from users.models import User
from .models import Friend
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import FriendsSerializer
from friends.permissions import IsAccountOwner, CheckIdOrNameIsDifferentFromYours
from rest_framework import generics
from rest_framework.views import Response, status

# Create your views here.


class FriendsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CheckIdOrNameIsDifferentFromYours]
    queryset = Friend.objects.all()
    serializer_class = FriendsSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        pk = kwargs["pk"]
        user2 = get_object_or_404(User, id=pk)
        if user == user2:
            return Response(
                {"message": "you can't send friend request to yourself!!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        friend_req = Friend.objects.filter(to_user=pk).first()
        if friend_req:
            return Response(
                {"message": "You already sent a friend request to this user!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        user2 = get_object_or_404(User, id=self.kwargs["pk"])
        serializer.save(to_user=user2, of=self.request.user.username)


class FriendsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Friend.objects.all()
    serializer_class = FriendsSerializer

    def update(self, request, *args, **kwargs):
        friend_request = get_object_or_404(Friend, id=self.kwargs["pk"])
        if friend_request.accepted:
            return Response(
                {"message": "this request has already been accepted!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not request.user == friend_request.to_user:
            return Response(
                {"message": "Only the requested user can accept the friend request!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(
            to_user=self.kwargs.get("pk"), request_user=self.request.user.username
        )

    lookup_url_kwarg = "pk"
