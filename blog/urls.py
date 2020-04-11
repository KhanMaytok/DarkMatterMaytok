from django.urls import path

from blog.views import get_blog_comments

urlpatterns = [
    path('post/<int:pk>/comments/', get_blog_comments, name='get_blog_comments'),
]

