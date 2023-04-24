from .models import Comment
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CommentsSerializer
from .permissions import IsAccountOwner
from rest_framework import generics

# Create your views here.


class CommentsView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer


class CommentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        return serializer.save(user_id=self.kwargs.get("pk"))

    lookup_url_kwarg = "pk"
