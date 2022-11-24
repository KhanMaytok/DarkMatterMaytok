from django.urls import path

from wiki.views import main

urlpatterns = [
    path('', main, name='main'),
]
