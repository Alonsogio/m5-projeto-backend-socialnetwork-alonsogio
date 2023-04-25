from django.db import models

# Create your models here.

class Messagers(models.Model):
    class Meta:
        ordering = ["id"]

    of = models.CharField(max_length=50)

    message_content = models.TextField(null=False)

    sent_on = models.DateTimeField(auto_now_add=True)

    to_user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="messagers"
    )

