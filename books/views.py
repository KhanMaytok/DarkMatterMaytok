from django.shortcuts import render, get_object_or_404

from books.models import Book, Chapter


def book_show(request, pk=None, slug=None):
    book = get_object_or_404(Book, pk=pk)

    return render(request, 'books/book.html', {'book': book})


def chapter_show(request, pk=None, slug=None, chapter_number=1):
    book = get_object_or_404(Book, pk=pk)
    chapter_number = get_object_or_404(Chapter, book=book, chapter_number=chapter_number)

    return render(request, 'books/chapter.html', {'book': book, 'chapter_number': chapter_number})
