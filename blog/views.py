from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

from blog.models import Post
from books.models import Book

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def home(request):
    books = Book.objects.all().values('id', 'cover', 'name', 'description', 'slug')
    posts = Post.objects.filter(created_at__lte=timezone.now())[:3]
    return render(request, 'blog/home.html', {'books': books, 'posts': posts})


@cache_page(CACHE_TTL)
def blog(request):
    post_list = Post.objects.filter(created_at__lte=timezone.now())
    paginator = Paginator(post_list, 7)

    posts = paginator.get_page(1)
    return render(request, 'blog/blog.html', {'posts': posts})


@cache_page(CACHE_TTL)
def blog_paginated(request, page=1):
    post_list = Post.objects.filter(created_at__lte=timezone.now())
    paginator = Paginator(post_list, 7)

    page_number = page
    posts = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'posts': posts})


def blog_post(request, pk=None, slug=None):
    post = get_object_or_404(Post, pk=pk)

    try:
        prev_post = Post.get_previous_by_created_at(post)
        if prev_post.created_at > timezone.now():
            prev_post = None
    except Post.DoesNotExist:
        prev_post = None
    try:
        next_post = Post.get_next_by_created_at(post)
        if next_post.created_at > timezone.now():
            next_post = None
    except Post.DoesNotExist:
        next_post = None

    return render(request, 'blog/post.html', {'post': post, 'prev_post': prev_post, 'next_post': next_post})
