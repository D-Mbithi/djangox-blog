from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email


class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to="avatar/", blank=True)
    about = models.TextField(max_length=500)
    user = models.OneToOneField(
        "accounts.CustomUser", on_delete=models.CASCADE, related_name="profile"
    )
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.full_name
