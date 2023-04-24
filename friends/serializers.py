import pdb
from rest_framework import serializers
from users.models import User
from .models import Friend
from django.shortcuts import get_object_or_404


class FriendsSerializer(serializers.ModelSerializer):
    def update(self, instance: Friend, validated_data: dict) -> Friend:
        if validated_data["accepted"] == True:
            user2 = get_object_or_404(User, username=instance.to_user)
            user1 = get_object_or_404(User, username=instance.of)
            test = Friend.objects.create(
                to_user=user1, of=user2.username, accepted=True
            )
            test.save()
        dados = []
        if "accepted" in validated_data:
            dados.append(validated_data.popitem())

        for key, value in dados:
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Friend
        fields = [
            "id",
            "to_user",
            "of",
            "accepted",
            "request_time",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "to_user": {"read_only": True},
            "of": {"read_only": True},
            "request_time": {"read_only": True},
        }
