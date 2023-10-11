from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    class ROLECHOICES(models.TextChoices):
        AUTHOR = "A", "Author"
        EDITOR = "E", "Editor"

    role = models.CharField(
        max_length=1,
        choices=ROLECHOICES.choices,
        default="A",
    )

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        "accounts.CustomUser", on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.CharField(max_length=500)
    avatar = models.ImageField(upload_to="avatars/", blank=True)

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse("accounts:profile", args=["id"])
