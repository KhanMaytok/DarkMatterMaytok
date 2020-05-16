from django.urls import path

from blog.views import home, blog, blog_post, blog_paginated

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('blog/page/<int:page>/', blog_paginated, name='blog_paginated'),
    path('blog/<int:pk>-<slug:slug>/', blog_post, name='blog_post'),
]
