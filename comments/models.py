from django.db import models
from model_utils.fields import UUIDField
from model_utils.models import TimeStampedModel

# Create your models here.


class Comment(TimeStampedModel):
    id = UUIDField(primary_key=True, version=4, editable=False)
    post = models.ForeignKey(
        "blog.Post", on_delete=models.CASCADE, related_name="comments"
    )
    comment = models.TextField(max_length=500)
    author = models.ForeignKey(
        "accounts.CustomUser",
        on_delete=models.CASCADE,
        related_name="comments",
    )

    def __str__(self):
        return self.id
