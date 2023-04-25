from rest_framework import serializers
from messagers.models import Messagers
 
class MessageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Messagers.objects.create(**validated_data)

    class Meta:
        model = Messagers
        fields = [
            "id",
            "message_content",
            "of",
            "sent_on",
            "to_user"
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "to_user": {"read_only": True},
            "of": {"read_only": True},
            "sent_on": {"read_only": True},
        }
