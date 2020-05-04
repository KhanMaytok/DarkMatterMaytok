from django.shortcuts import render, get_object_or_404
from django.conf import settings
from books.models import Book, Chapter
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def book_show(request, pk=None, slug=None):
    book = get_object_or_404(Book, pk=pk)

    return render(request, 'books/book.html', {'book': book})


@cache_page(CACHE_TTL)
def chapter_show(request, pk=None, slug=None, chapter_number=1):
    book = get_object_or_404(Book, pk=pk)
    chapter = get_object_or_404(Chapter, book=book, chapter_number=chapter_number)

    return render(request, 'books/chapter.html', {'book': book, 'chapter': chapter})
