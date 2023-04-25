from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "name", "members", "created_at"]


extra_kwargs = {
    "id": {"read_only": True},
    "creator": {"read_only": True},
    "created_at": {"read_only": True},
}
