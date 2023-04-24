from django.db import models

# Create your models here.


class Comment(models.Model):
    class Meta:
        ordering = ["id"]

    comment_content = models.TextField(null=False)

    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="comments"
    )
