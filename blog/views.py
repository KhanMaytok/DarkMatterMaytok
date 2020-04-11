from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404

from blog.models import Post, Comment


def get_blog_comments(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    post_type = ContentType.objects.get(app_label='blog', model='post')
    comments = Comment.objects.filter(content_type=post_type, object_id=post.pk)

    return render(request, 'blog/blog_comments.html', {'comments': comments})
