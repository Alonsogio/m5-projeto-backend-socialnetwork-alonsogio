# Generated by Django 4.1.7 on 2023-03-12 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("likes", "0001_initial"),
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="like",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="likes",
                to="posts.post",
            ),
        ),
    ]
