from accounts.views import profile
from django.urls import path

app_name = "accounts"


urlpatterns = [path("profile/", profile, name="profile")]
