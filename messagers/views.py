import pdb
from django.shortcuts import get_object_or_404
from posts.permissions import IsAccountOwner
from users.models import User
from .models import Messagers
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import MessageSerializer
from rest_framework import generics

# Create your views here.

class MessagesView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = Messagers.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        user2 = get_object_or_404(User, id=self.kwargs["pk"])
        serializer.save(to_user=user2, of=self.request.user.username)