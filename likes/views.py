from .models import Like
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import LikesSerializer
from .permissions import IsAccountOwner
from rest_framework import generics

# Create your views here.


class LikesView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikesSerializer


class LikesDetailView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Like.objects.all()
    serializer_class = LikesSerializer

    def perform_create(self, serializer):
        return serializer.save(user_id=self.kwargs.get("pk"))

    lookup_url_kwarg = "pk"
