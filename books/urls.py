from django.urls import path, include
from rest_framework import routers

from books import api
from books.views import book_show, chapter_show, board_show

router = routers.DefaultRouter()

router.register(r'gladiator', api.GladiatorViewSet)

urlpatterns = [
    path('<int:pk>-<slug:slug>/', book_show, name='book_show'),
    path('<int:pk>-<slug:slug>/<int:chapter_number>/', chapter_show, name='chapter_show'),
    path('board/<int:pk>/', board_show, name='board_show'),
    path('board/<int:pk>/', board_show, name='board_list'),

    # API
    path('api/', include(router.urls)),
]
