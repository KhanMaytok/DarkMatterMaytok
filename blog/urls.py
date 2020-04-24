from django.urls import path

from blog.views import home, blog, blog_post

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('blog/page/<int:page>/', blog, name='blog'),
    path('blog/posts/<int:pk>-<slug:slug>/', blog_post, name='blog_post'),
]
