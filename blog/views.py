from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from DarkMatterMaytok.settings import PAGE_SIZE
from blog.models import Post
from books.models import Book


def home(request):
    books = Book.objects.all()
    posts = get_post_list(request)[:3]
    return render(request, 'blog/home.html', {'books': books, 'posts': posts})


def blog(request):
    post_list = get_post_list(request)
    paginator = Paginator(post_list, PAGE_SIZE)

    posts = paginator.get_page(1)
    return render(request, 'blog/blog.html', {'posts': posts})


def blog_paginated(request, page=1):
    post_list = get_post_list(request)
    paginator = Paginator(post_list, PAGE_SIZE)

    page_number = page
    posts = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'posts': posts})


def blog_post(request, pk=None, *args, **kwargs):
    if request.user.is_superuser is True:
        post = get_object_or_404(Post, pk=pk, is_draft=False)
    else:
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


def get_post_list(request):
    return Post.objects.filter(created_at__lte=timezone.now(), is_draft=False)


def user_is_founder(user):
    return user.is_founder is True or user.is_superuser
