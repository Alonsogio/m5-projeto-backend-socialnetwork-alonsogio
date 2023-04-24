from rest_framework import serializers

from .models import Like


class LikesSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Like.objects.create(**validated_data)

    class Meta:
        model = Like
        fields = [
            "id",
            "user_id",
            "post_id",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "user_id": {"read_only": True},
            "post_id": {"read_only": True},
        }
