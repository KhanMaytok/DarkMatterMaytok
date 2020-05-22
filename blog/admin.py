from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    exclude = ['user']

    def get_form(self, request, *args, **kwargs):
        form = super(PostAdmin, self).get_form(request, *args, **kwargs)
        form.user = request.user
        return form


admin.site.register(Post, PostAdmin)
