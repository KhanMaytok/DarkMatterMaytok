from django.contrib import admin
from django_comments.models import Comment
from django_comments_xtd.models import XtdComment

from core.models import User

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(XtdComment)
