from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post, Project


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    exclude = ['user', 'slug']

    def get_form(self, request, obj=None, change=False, **kwargs):
        if obj is not None:
            obj.user = request.user
        return super().get_form(request, obj, **kwargs)


class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('log',)
    exclude = ['user', 'slug']

    def get_form(self, request, obj=None, change=False, **kwargs):
        if obj is not None:
            obj.user = request.user
        return super().get_form(request, obj, **kwargs)


admin.site.register(Post, PostAdmin)
admin.site.register(Project, ProjectAdmin)
