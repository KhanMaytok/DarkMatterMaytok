from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.utils import user_has_min_rank
from books.models import Book, Chapter, Board, Gladiator


def book_show(request, pk=None, slug=None):
    book = get_object_or_404(Book, pk=pk)

    return render(request, 'books/book.html', {'book': book})


def chapter_show(request, pk=None, slug=None, chapter_number=1):
    book = get_object_or_404(Book, pk=pk)
    chapter = get_object_or_404(Chapter, book=book, chapter_number=chapter_number)

    if chapter.rank_required != 'C' and not request.user.is_authenticated:
        return HttpResponse(
            'El capítulo está en estado Beta. Solo miembros con acceso pueden leerlo. ¿Quizá necesitas <a href="/login">Iniciar sesión?</a>')

    # Check if the user has permissions
    if not user_has_min_rank(request.user, chapter.rank_required):
        return HttpResponse("Lo sentimos. Aún no tienes el rango para leer este capítulo.")

    return render(request, 'books/chapter.html', {'book': book, 'chapter': chapter})


def board_show(request, pk=None):
    board = get_object_or_404(Board, pk=pk)

    return render(request, 'books/board.html', {'post': board, 'prev_post': None, 'next_post': None})


def gladiators(request):
    g = Gladiator.objects.all()

    return render(request, 'books/gladiators.html', {'gladiators': g})
