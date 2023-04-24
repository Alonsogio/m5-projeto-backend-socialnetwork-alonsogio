from rest_framework import serializers

from .models import Comment


class CommentsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance: Comment, validated_data: dict) -> Comment:
        for key, value in validated_data.items():
            setattr(instance, key, value)
            # if key == "password":
            #     instance.set_password(value)
        instance.save()

        return instance

    class Meta:
        model = Comment
        fields = [
            "id",
            "user_id",
            "post_id",
            "created_time",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "user_id": {"read_only": True},
            "created_time": {"read_only": True},
        }
