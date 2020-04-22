from django.urls import path

from blog.views import home, blog

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('blog/page/<int:page>/', blog, name='blog'),
]
