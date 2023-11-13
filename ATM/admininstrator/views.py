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

def adminLogin(request):
    renderData = {
        'request': request,
        'path': 'administrator/admin-login.html',
        'context': { 
            'form': AdminLoginForm(),
            'message': '',
        } 
    } 
    if request.method == 'POST': 
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            admin = getAdmin(form.cleaned_data['username'])
            if not admin: 
                setContextMessage(renderData['context'], 'Not a valid administrator')
                return renderPage(renderData)
            
            if admin.password != form.cleaned_data['password']: 
                setContextMessage(renderData['context'], 'Incorrect password')
                return renderPage(renderData)
            
            request.session['admin-token'] = admin.username
            return redirect('/administrator')
        else: 
            setContextMessage(renderData['context'], 'Form not valid')
            return renderPage(renderData)
    else:
        admin = Admin(
            username = 'admin', 
            password = 'admin'
        )
        admin.save()
        return renderPage(renderData)

@login_required
def adminLogout(request):
    logout(request)
    return redirect('admin-login')

@staff_member_required
def atmMachineStatus(request):
    atm_machine = ATMMachine.objects.get(atm_machine_uid = request.session['machine'])

    context = {
        'status': atm_machine.status,
        'atm_machine_uid': atm_machine.atm_machine_uid,
        'current_balance': atm_machine.current_balance,
        'mininum_balance':atm_machine.minimum_balance,
        'location':atm_machine.location,
    }
    return render(request,'admininstrator/atm-machine-status.html', context)

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