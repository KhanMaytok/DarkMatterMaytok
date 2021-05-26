import json

from django.contrib import admin

from django_json_widget.widgets import JSONEditorWidget
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.postgres.fields import JSONField
from books.models import Book, Chapter, Board


class ChapterAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


admin.site.register(Book)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Board)
