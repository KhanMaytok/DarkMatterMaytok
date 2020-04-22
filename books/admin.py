from django.contrib import admin

from books.models import Book, Chapter

admin.site.register(Book)
admin.site.register(Chapter)
