from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from comments.serializers import CommentsSerializer

from followers.serializers import FollowersSerializer
from posts.serializers import PostsSerializer
from .models import User
from friends.serializers import FriendsSerializer


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)
            if key == "password":
                instance.set_password(value)
        instance.save()

        return instance

    friends = FriendsSerializer(many=True, read_only=True)
    followers = FollowersSerializer(many=True, read_only=True)
    posts = PostsSerializer(many=True, read_only=True)
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "followers",
            "friends",
            "posts",
            "comments",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ],
            },
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                    )
                ],
            },
        }
