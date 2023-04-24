from django.shortcuts import get_object_or_404
from users.models import User
from .models import Follower
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import FollowersSerializer
from .permissions import IsAccountOwner
from rest_framework import generics
from rest_framework.views import Response, status

# Create your views here.


class FollowersView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = Follower.objects.all()
    serializer_class = FollowersSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        pk = kwargs["pk"]
        user2 = get_object_or_404(User, id=pk)
        if user == user2:
            return Response(
                {"message": "You cannot follow yourself!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        friend_req = Follower.objects.filter(to_user_id=pk).first()
        if friend_req:
            return Response(
                {"message": "You already follow this user!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        user2 = get_object_or_404(User, id=self.kwargs["pk"])
        serializer.save(to_user_id=user2.id, of=self.request.user.username)


class FollowersDetailView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Follower.objects.all()
    serializer_class = FollowersSerializer

    def perform_create(self, serializer):
        return serializer.save(to_user_id=self.kwargs.get("pk"))

    lookup_url_kwarg = "pk"
