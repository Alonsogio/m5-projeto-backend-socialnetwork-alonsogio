from django.db import models

# Create your models here.


class Privacy(models.TextChoices):
    Public = "Public"
    Private = "Private"


class Post(models.Model):
    class Meta:
        ordering = ["id"]

    post_content = models.TextField(null=False)

    publication_privacy = models.CharField(
        max_length=20,
        choices=Privacy.choices,
        default=Privacy.Public,
    )

    published_in = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts"
    )
