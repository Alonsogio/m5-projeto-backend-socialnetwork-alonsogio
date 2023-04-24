import pdb
from rest_framework import serializers
from comments.serializers import CommentsSerializer
from likes.serializers import LikesSerializer


from .models import Post, Privacy


class PostsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance: Post, validated_data: dict) -> Post:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance

    likes = LikesSerializer(many=True, read_only=True)
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "post_content",
            "publication_privacy",
            "published_in",
            "likes",
            "comments",
            "user_id",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "user_id": {"read_only": True},
            "published_in": {"read_only": True},
            "publication_privacy": {"choices": Privacy.choices},
        }
