from django.db import models
from django.utils import timezone
from users.models import User

class Room(models.Model):
    creator = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='created_rooms')
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='rooms')
    created_at = models.DateTimeField(default=timezone.now)
