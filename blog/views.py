from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from DarkMatterMaytok.settings import PAGE_SIZE
from blog.models import Post, Project, ProjectUser
from books.models import Book
from core.models import User


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
        post = get_object_or_404(Post, pk=pk)
    else:
        post = get_object_or_404(Post, pk=pk, is_draft=False)

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

    project_users = None
    if post.project is not None:
        project_users = ProjectUser.objects.filter(project=post.project).order_by('-amount')
        count = project_users.count()
        if count > 5:
            project_users = project_users[:5]

    return render(request, 'blog/post.html',
                  {'post': post, 'prev_post': prev_post, 'next_post': next_post, 'project_users': project_users})


def get_post_list(request):
    return Post.objects.filter(created_at__lte=timezone.now(), is_draft=False)


def user_is_founder(user):
    return user.is_founder is True or user.is_superuser


@login_required
def fund_project(request, project_id, amount):
    user: User = request.user
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return JsonResponse({'total': 0, 'error': True})

    try:
        amount = int(amount)
    except ValueError:
        return JsonResponse({'total': 0, 'error': True})

    if user.balance < amount:
        return JsonResponse({'total': 0, 'error': True})

    project_user, _ = ProjectUser.objects.get_or_create(project=project, user=request.user)
    project_user.amount += amount
    project_user.save()

    user.balance -= amount
    user.save()

    all_funds = ProjectUser.objects.filter(project=project).aggregate(Sum('amount'))['amount__sum']
    project.amount = all_funds
    project.save()

    return JsonResponse({'total': all_funds, 'error': False})
