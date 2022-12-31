from django.shortcuts import render
from django.urls import reverse

from .forms import CommentForm
from .models import Post, Comment


# Create your views here.
def index(request):
    return render(request, "blog/index.html", {
        "posts": Post.objects.all().order_by('-created_on')
    })


def category(request, category):
    return render(request, "blog/category.html", {
        "posts": Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    })


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post
            )
            comment.save()
    return render(request, "blog/blog_detail.html", {
        "post": post,
        "comments": Comment.objects.filter(post=post),
        "form": form,
    })
