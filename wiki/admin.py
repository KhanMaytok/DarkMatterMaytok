from django.db import models
from django.contrib import admin

from martor.widgets import AdminMartorWidget

from wiki.models import Article


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


admin.site.register(Article, ArticleAdmin)
