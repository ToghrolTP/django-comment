from django.shortcuts import render
from .models import Post


def home(request):
    available_posts = Post.published.all()

    context = {
        "posts": available_posts,
    }
    return render(request, "blog/home.html", context)


def post_list(request, slug):
    post = Post.objects.get(slug=slug)

    context = {
        "post": post,
    }
    return render(request, "blog/post_list.html", context)
