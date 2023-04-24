from rest_framework import serializers

from .models import Follower


class FollowersSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Follower.objects.create(**validated_data)

    class Meta:
        model = Follower
        fields = [
            "id",
            "to_user_id",
            "of",
            "request_time",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "to_user_id": {"read_only": True},
            "of": {"read_only": True},
            "request_time": {"read_only": True},
        }
