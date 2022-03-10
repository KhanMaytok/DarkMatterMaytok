from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.decorators.cache import cache_page

from blog.models import Post
from books.models import Book


def home(request):
    books = Book.objects.all()
    posts = Post.objects.filter(created_at__lte=timezone.now(), is_draft=False)[:3]
    webpush = {"group": 'homelander'}
    return render(request, 'blog/home.html', {'books': books, 'posts': posts, "webpush": webpush})


def blog(request):
    post_list = Post.objects.filter(created_at__lte=timezone.now(), is_draft=False)
    paginator = Paginator(post_list, 7)

    posts = paginator.get_page(1)
    return render(request, 'blog/blog.html', {'posts': posts})


def blog_paginated(request, page=1):
    post_list = Post.objects.filter(created_at__lte=timezone.now(), is_draft=False)
    paginator = Paginator(post_list, 7)

    page_number = page
    posts = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'posts': posts})


def blog_post(request, pk=None, slug=None):
    post = get_object_or_404(Post, pk=pk)

    try:
        prev_post = Post.get_previous_by_created_at(post)
        if prev_post.created_at > timezone.now() or prev_post.is_draft is True:
            prev_post = None
    except Post.DoesNotExist:
        prev_post = None
    try:
        next_post = Post.get_next_by_created_at(post)
        if next_post.created_at > timezone.now() or next_post.is_draft is True:
            next_post = None
    except Post.DoesNotExist:
        next_post = None

    return render(request, 'blog/post.html', {'post': post, 'prev_post': prev_post, 'next_post': next_post})
