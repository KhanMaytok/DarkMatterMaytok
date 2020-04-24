from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from blog.models import Post
from books.models import Book


def home(request):
    books = Book.objects.all().values('id', 'cover', 'name', 'description')
    posts = Post.objects.all()[:3]
    return render(request, 'blog/home.html', {'books': books, 'posts': posts})


def blog(request, page=1):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 7)

    page_number = page
    posts = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'posts': posts})


def blog_post(request, pk=None, slug=None):
    post = get_object_or_404(Post, pk=pk, slug=slug)
    return render(request, 'blog/post.html', {'post': post})
