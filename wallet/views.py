from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render

from wallet.models import Debt


@login_required
def home(request):
    debts = Debt.objects.all().aggregate(Sum('debts'))
    return render(request, 'wallet/home.html', {'debts': debts})
