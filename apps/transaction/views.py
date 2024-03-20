from django.shortcuts import render,redirect
from .models import Transaction
from django.utils import timezone
# Create your views here.


def pay(request):
    if request.method == 'POST':
        details = request.POST.get('details')
        user = request.user
        if user.is_authenticated:
            new_transaction = Transaction.objects.create(
                user=user,
                date=timezone.now(),
                details=details,
                status=Transaction.status,
            )
            return redirect('http://localhost:8000/end_transaction')
    return render(request, 'transaction/pay.html')

def end_transaction(request):
    return render(request, 'transaction/end_transaction.html')