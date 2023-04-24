import pdb
from django.forms import model_to_dict
from friends.models import Friend
from rest_framework.views import Response, status
from users.models import User
from followers.models import Follower
from .models import Post
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import PostsSerializer
from .permissions import IsAccountOwner
from rest_framework import generics

# Create your views here.


class PostsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

    # def list(self, request, *args, **kwargs):
    #     # user3 = Post.objects.all()
    #     # for user_id in user3:
    #     #     user_dict = model_to_dict(user_id)

    #     # user2 = User.objects.filter(id=user_dict["user"]).first()
    #     # followers = Follower.objects.filter(to_user_id=user2.id).first()
    #     # friends = Friend.objects.filter(to_user_id=user2.id).first()
    #     # posts = Post.objects.filter(user_id=user2.id).first()

    #     public = []

    #     user1 = Post.objects.all()
    #     for publication_privacy in user1:
    #         # public_dict = model_to_dict(publication_privacy)

    #         user2 = User.objects.filter(id=publication_privacy.user_id)
    #         for user in user2:
    #             follo = Follower.objects.filter(to_user=user.id).first()
    #             fri = Friend.objects.filter(to_user=user.id).first()

    #         if publication_privacy.publication_privacy == "Public":
    #             public.append(publication_privacy)

    #         if publication_privacy.publication_privacy == "Private":
    #             if (
    #                 follo.of == self.request.user.username
    #                 or fri.of == self.request.user.username
    #             ):
    #                 public.append(publication_privacy)

    #         serializer = PostsSerializer(public, many=True)
    #         # pdb.set_trace()
    #         return Response(serializer.data, status.HTTP_200_OK)
    #     return super().list(request, *args, **kwargs)

    # pdb.set_trace()

    # post = get_object_or_404(Post, id=self.kwargs["pk"])
    # user2 = User.objects.filter(id=post.user_id)
    # followers = Follower.objects.filter(to_user_id=user2.id)
    # friends = Friend.objects.filter(to_user_id=user2.id)

    # if public_dict["publication_privacy"] == "Public":
    #     post_no_aut_user = Post.objects.filter(publication_privacy="Public")
    #     public.append(post_no_aut_user)
    #     serializer = PostsSerializer(post_no_aut_user, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)
    #     return super().list(request, *args, **kwargs)

    # if (
    #     user_dict["publication_privacy"] == "Private"
    #     and followers.of == self.request.user.username
    #     or friends.of == self.request.user.username
    #     and friends.accepted == True
    # ):
    #     post_no_aut_user = Post.objects.all()
    #     serializer = PostsSerializer(post_no_aut_user, many=True)
    #     return super().list(request, *args, **kwargs)
    # return Response(serializer.data, status.HTTP_200_OK)

    # if self.request.user.is_authenticated == False:
    #     post_no_aut_user = Post.objects.filter(publication_privacy="Private")
    #     serializer = PostsSerializer(post_no_aut_user, many=True)

    #     return Response(serializer.data, status.HTTP_200_OK)
    # else:
    # return super().list(request, *args, **kwargs)
    #

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class PostsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Post.objects.all()
    serializer_class = PostsSerializer

    lookup_url_kwarg = "pk"
