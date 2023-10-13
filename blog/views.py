from django.core.paginator import EmptyPage, Page, Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import PostForm
from .models import Post

# Create your views here.


def post_list(request):
    """Get all blog post."""
    qs = Post.objects.all()

    paginator = Paginator(qs, 10)
    page_number = request.GET.get("page")

    posts = paginator.get_page(page_number)

    template = "blog/index.html"
    context = {"posts": posts}

    return render(request, template, context)


def post_detail(request, post_id):
    """Get blog post by Id."""
    post = get_object_or_404(Post, uuid=post_id)
    template = "blog/single.html"
    context = {"post": post}

    return render(request, template, context)


def post_create(request):
    """Create new blog post."""
    if request.method == "POST":
        form = PostForm()
        if form.is_valid():
            pass
    else:
        form = PostForm()

    template = "blog/post_create.html"

    context = {"form": form}

    return render(request, template, context)


def post_update(request, post_id):
    """Update blog post by Id."""
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm()

        if form.is_valid():
            pass
    else:
        form = PostForm(instance=post)
    template = "blog/post_create.html"

    context = {"form": form}

    return render(request, template, context)


def post_delete(request, post_id):
    """Get blog post by Id."""
    post = get_object_or_404(Post, id=post_id)
    post.delete()

    return redirect(reverse("blog:post_list"))
