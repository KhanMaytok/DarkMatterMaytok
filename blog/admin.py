from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.db import models
from django.forms import Textarea
from blog.models import Post


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'style': 'width: 100%;'})},
    }


admin.site.register(Post, PostAdmin)
