from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404

from blog.models import Post


def home(request):
    return render(request, 'blog/home.html')
