from django.urls import path

from blog.views import home, blog, blog_post, blog_paginated, fund_project

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('blog/page/<int:page>/', blog_paginated, name='blog_paginated'),
    path('blog/<int:pk>-<slug:slug>/', blog_post, name='blog_post'),
    path('blog/project/<int:project_id>/fund/<int:amount>/', fund_project, name='fund_project'),
]
