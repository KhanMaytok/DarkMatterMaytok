from django.shortcuts import render, get_object_or_404

from books.models import Book


def book_show(request, pk=None, slug=None):
    book = get_object_or_404(Book, pk=pk)

    return render(request, 'blog/blog_comments.html', {'book': book})
