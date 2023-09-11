# Generated by Django 4.2 on 2023-09-10 11:32

from django.db import migrations
import model_utils.fields
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name_plural": "Post"},
        ),
        migrations.RemoveField(
            model_name="category",
            name="id",
        ),
        migrations.RemoveField(
            model_name="post",
            name="id",
        ),
        migrations.AddField(
            model_name="category",
            name="uuid",
            field=model_utils.fields.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="uuid",
            field=model_utils.fields.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
