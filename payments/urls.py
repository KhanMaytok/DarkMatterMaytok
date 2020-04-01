from django.urls import path

from payments.views import create_payment

urlpatterns = [
    path('create/', create_payment, name='create_payment'),
]
