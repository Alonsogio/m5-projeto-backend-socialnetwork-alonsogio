from django.db import models

# Create your models here.

from django.db import models


class Friend(models.Model):
    class Meta:
        ordering = ["id"]

    of = models.CharField(max_length=255)

    id_request_friend = models.IntegerField()

    request_time = models.DateTimeField(auto_now_add=True)

    accepted = models.BooleanField(default=False)

    to_user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="friends",
    )
