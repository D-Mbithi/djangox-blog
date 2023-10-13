from blog import views
from django.urls import path

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("create/", views.post_create, name="post_create"),
    path("<uuid:post_id>/", views.post_detail, name="post_detail"),
    path("<uuid:post_id>/update/", views.post_update, name="post_update"),
    path("<uuid:post_id>/delete/", views.post_delete, name="post_delete"),
]
