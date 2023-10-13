from django.contrib import admin

from .models import Category, Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "category",
        "created",
        "modified",
        "status",
    ]
    prepopulated_fields = {
        "slug": ["title"],
    }
    list_filter = ["status"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
