from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD:ATM/Transactions/views.py
from .models import ATMUser, BankAccount, Transaction, TransactionType
from .forms import DepositForm, TransferForm, WithdrawalForm, ChangePinForm, PaymentForm
=======
from django.contrib.auth import authenticate, login
from .models import BankAccount, Transaction, Receipt, ATMUser, TransactionType, Payment
from .forms import DepositForm, TransferForm, WithdrawalForm, PaymentForm, ChangePinForm, BalanceInquiryForm
from admininstrator.models import ATMMachine
>>>>>>> af86f505fdc167d543197ee3574853e13f90d992:ATM/transaction/views.py

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        user = request.user
        amount = form.cleaned_data['amount']
        account = BankAccount.objects.get(holders=user)
        account.balance += amount
        account.save()
        Transaction.objects.create(amount=amount, type=TransactionType.objects.get(name='Deposit'), recipientIBAN=account.IBAN)
        # Crie um objeto Receipt e salve os detalhes do recibo
        return redirect('success_page')
    else:
        form = DepositForm()
    return render(request, 'deposit.html', {'form': form})

@login_required
def transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        recipientIBAN = form.cleaned_data['recipientIBAN']
        amount = form.cleaned_data['amount']
        sender_account = BankAccount.objects.get(holders=request.user)
        recipient_account = BankAccount.objects.get(IBAN=recipientIBAN)
        if sender_account.balance >= amount:
            sender_account.balance -= amount
            sender_account.save()
            recipient_account.balance += amount
            recipient_account.save()
            Transaction.objects.create(user=request.user, type=TransactionType.objects.get(name='Transfer'), amount=amount, recipientIBAN=recipientIBAN)
            # Crie um objeto Receipt e salve os detalhes do recibo
            return redirect('success_page')
        else:
            return render(request, 'error_page.html', {'error_message': 'Insufficient funds'})
    else:
        form = TransferForm()
    return render(request, 'transfer.html', {'form': form})

@login_required
def withdrawal(request):
    if request.method == 'POST':
        form = WithdrawalForm(request.POST)
        amount = form.cleaned_data['amount']
        account = BankAccount.objects.get(holders=request.user)
        if account.balance >= amount:
            account.balance -= amount
            account.save()
            Transaction.objects.create(user=request.user, type=TransactionType.objects.get(name='Withdrawal'), amount=amount)
            # Crie um objeto Receipt e salve os detalhes do recibo
            return redirect('success_page')
        else:
            return render(request, 'error_page.html', {'error_message': 'Insufficient funds'})
    else:
        form = WithdrawalForm()
    return render(request, 'withdrawal.html', {'form': form})

@login_required
def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
<<<<<<< HEAD:ATM/Transactions/views.py
        entity = form.cleaned_data['entity']
        reference = form.cleaned_data['reference']
        amount = form.cleaned_data['amount']
        bank_account = BankAccount.objects.get(holders=request.user)

        if bank_account.balance >= amount:
            # Crie um objeto Payment e salve os detalhes do pagamento
            bank_account.balance -= amount
            bank_account.save()
            return redirect('payment_success_view')
        else:
            return render(request, 'error_page.html', {'error_message': 'Insufficient funds'})
    else:
        form = PaymentForm()
    return render(request, 'payment/make_payment.html', {'form': form})
=======
        if form.is_valid():
            entity = form.cleaned_data['entity']
            reference = form.cleaned_data['reference']
            amount = form.cleaned_data['amount']
            type = form.cleaned_data['type']#adicionar ao html
            
            bank_account = BankAccount.objects.get(user=request.user)  

            if bank_account.balance >= amount:
                transaction = Transaction.objects.get_or_create(amount = amount,
                                                                type = type)
                latest_trans = Transaction.objects.filter().latest()
                
                payment = Payment(entity=entity, reference=reference,
                                   amount=amount, 
                                   transaction_id = latest_trans.objects.order_by('transaction_id')[0])
                payment.save()


                bank_account.balance -= amount
                bank_account.save()
                Receipt.objects.create(content=f"Paid ${amount} to {entity}", 
                                       transaction_id=Transaction.objects.filter(user=request.user).last(),
                                       transaction_type = type, user_id=request.user)
                
                return redirect('payment_success_view') 
            else:
                return render(request, 'error_page.html', {'error_message': 'Insufficient funds'}) #Do the error_page.html?????
        else:
            return render(request, 'error_page.html', {'error_message': 'Payment form not valid'}) 
>>>>>>> af86f505fdc167d543197ee3574853e13f90d992:ATM/transaction/views.py

@login_required
def change_pin(request):
    if request.method == 'POST':
        form = ChangePinForm(request.POST)
        current_pin = form.cleaned_data['current_pin']
        new_pin = form.cleaned_data['new_pin']
        confirm_new_pin = form.cleaned_data['confirm_new_pin']
        user = request.user
        atm_user = ATMUser.objects.get(user=user)
        if atm_user.pin == current_pin:
            if new_pin == confirm_new_pin:
                atm_user.pin = new_pin
                atm_user.save()
                return redirect('success_page')
            else:
                return render(request, 'error_page.html', {'error_message': 'PIN does not match'})
        else:
            return render(request, 'error_page.html', {'error_message': 'Current PIN is incorrect'})
    else:
        form = ChangePinForm()
    return render(request, 'change_pin.html', {'form': form})

@login_required
def balance_inquiry(request):
    account = BankAccount.objects.get(holders=request.user)
    return render(request, 'balance_inquiry.html', {'balance': account.balance})

@login_required
def transaction_history(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transaction_history.html', {'transactions': transactions})

@login_required
def success_page(request):
    return render(request, 'success_page.html')

@login_required
def error_page(request):
    error_message = "Ocorreu um erro inesperado."
    return render(request, 'error_page.html', {'error_message': error_message})