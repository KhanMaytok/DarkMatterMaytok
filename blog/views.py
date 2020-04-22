from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from blog.models import Post


def home(request):
    return render(request, 'blog/home.html')


def blog(request, page=1):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 7)

    page_number = page
    posts = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'posts': posts})
