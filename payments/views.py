import requests
from django.http import JsonResponse

from DarkMatterMaytok.settings import CULQI_PUBLIC_KEY, CULQI_PRIVATE_KEY


def create_payment(request):
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {CULQI_PRIVATE_KEY}",
    }

    payload = {
        "amount": "500",
        "currency_code": "PEN",
        "email": "khan.maytok@gmail.com",
        "source_id": request.GET.get('token', None),
    }

    return JsonResponse({'ja': 90})
