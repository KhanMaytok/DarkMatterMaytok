from django.urls import path

from wallet.views import home

app_name = 'wallet'
urlpatterns = [
    path('', home, name='home'),
]
