from django.db import models

# Create your models here.


class Like(models.Model):
    class Meta:
        ordering = ["id"]

    post = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="likes"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="likes"
    )
