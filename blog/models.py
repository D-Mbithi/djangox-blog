from django.db import models
from django.contrib.auth import get_user_model
from model_utils.fields import UUIDField
from taggit.managers import TaggableManager


User = get_user_model()


class Post(models.Model):
    """Model defining blog post"""

    STATUSCHOICE = (("d", "Draft"), ("p", "Published"))

    uuid = UUIDField(primary_key=True, version=4, editable=False)
    title = models.CharField(max_length=200)
    post = models.TextField()
    status = models.CharField(max_length=100, choices=STATUSCHOICE, default="d")
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="blog")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name_plural = "Post"

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    """Model defination for Categories."""

    uuid = UUIDField(primary_key=True, version=4, editable=False)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name
