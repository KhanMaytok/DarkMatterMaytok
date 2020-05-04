from django.urls import path

from books.views import book_show, chapter_show

urlpatterns = [
    path('<int:pk>-<slug:slug>/', book_show, name='book_show'),
    path('<int:pk>-<slug:slug>/<int:chapter_number>/', chapter_show, name='chapter_show'),
]
