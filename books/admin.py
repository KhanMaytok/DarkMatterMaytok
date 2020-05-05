from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from books.models import Book, Chapter


class ChapterAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Book)
admin.site.register(Chapter, ChapterAdmin)
