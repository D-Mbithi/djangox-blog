from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from model_utils.fields import UUIDField
from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

User = get_user_model()


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Post(TimeStampedModel):
    """Model defining blog post"""

    STATUSCHOICE = (("d", "Draft"), ("p", "Published"))

    uuid = UUIDField(primary_key=True, version=4, editable=False)
    title = models.CharField(max_length=200)
    post = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True)
    status = models.CharField(
        max_length=100,
        choices=STATUSCHOICE,
        default="d",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name="blog",
    )
    tags = TaggableManager(through=UUIDTaggedItem, blank=True)
    category = models.ForeignKey(
        "blog.Category",
        on_delete=models.CASCADE,
        related_name="posts",
    )

    class Meta:
        verbose_name_plural = "Post"
        ordering = ("-created",)

    def __str__(self) -> str:
        return str(self.title)

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"post_id": self.uuid})


class Category(TimeStampedModel):
    """Model defination for Categories."""

    uuid = UUIDField(primary_key=True, version=4, editable=False)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return str(self.name)
