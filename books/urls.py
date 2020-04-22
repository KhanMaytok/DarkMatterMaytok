from django.urls import path

from books.views import book_show

urlpatterns = [
    path('<int:pk>-<slug:slug>/', book_show, name='book_show'),
]
