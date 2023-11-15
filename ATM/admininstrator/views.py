from django.shortcuts import render, redirect
from .forms import AdminLoginForm,TransactionSearchForm
from transaction.models import Transaction
from django.http import HttpResponse
from admininstrator.models import Admin
from ATM.services import getAdmin, setContextMessage, renderPage
from .models import ATMMachine
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def home(request):
    return render(request,'admininstrator/base.html')


@staff_member_required
def atmMachineStatus(request):
    atm_machine = ATMMachine.objects.all()

    context = { 'atm_machines': atm_machine,} 
    return render(request,'admininstrator/atm-machine-status.html', context)

@staff_member_required
def view_transaction_history(request):
    form = TransactionSearchForm(request.POST or None)
    history = None
    message = None

    if request.method == 'POST' and form.is_valid():
        recipient_iban = form.cleaned_data['recipient_iban']
        history = Transaction.objects.filter(recipient_iban=recipient_iban)

        if not history.exists():
            message = f'No transaction found for that IBAN:{recipient_iban}'

    context = {
        'form':form,
        'history':history,
        'message':message
    }
    return render(request,'admininstrator/view-transaction-history.html',context)


def update_status(request,atm_machine_uid):
    if request.method == 'POST':
        new_status = request.POST.get('status')
        atm_machine = ATMMachine.objects.get(atm_machine_uid=atm_machine_uid)
        atm_machine.status = new_status
        atm_machine.save()
    return redirect('atm-machine-status')