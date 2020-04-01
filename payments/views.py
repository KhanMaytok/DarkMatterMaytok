from culqi.client import Culqi
from django.http import JsonResponse
from django.shortcuts import render

from DarkMatterMaytok.settings import CULQI_PUBLIC_KEY, CULQI_PRIVATE_KEY


def create_payment(request):
    culqi = Culqi(public_key=CULQI_PUBLIC_KEY, private_key=CULQI_PRIVATE_KEY)

    response = culqi.charge.create({
        "amount": 500,
        "currency_code": "PEN",
        "description": "Donación fantástica",
        "email": "richard@piedpiper.com",
        "source_id": request.GET.get('id'),
    })

    return JsonResponse({'ja': 90})
