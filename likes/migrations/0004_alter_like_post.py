# Generated by Django 4.1.7 on 2023-03-18 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_initial"),
        ("likes", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="likes_posts",
                to="posts.post",
            ),
        ),
    ]
