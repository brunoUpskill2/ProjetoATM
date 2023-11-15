from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import BankAccount, Transaction, TransactionType, Payment,  Withdrawal, Deposit, Transfer
from .forms import DepositForm, TransferForm, WithdrawalForm, PaymentForm
from user.models import ATMUser
@login_required
def home(request):
    return render(request, 'transactions/home.html')

@login_required
def deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST or None)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            type = form.cleaned_data['type']
            bank_account = BankAccount.objects.get(user=request.user)
            bank_account.balance += amount
            bank_account.save()

            Transaction.objects.get_or_create(amount = amount,
                                              account = bank_account,
                                              content = f'Deposited {amount} in account IBAN {bank_account}'
                                              )
                                                            
            deposit = Deposit(amount=amount, account=BankAccount.objects.get(user=request.user),
                              transaction_id = Transaction.objects.latest())
            
            deposit.save()
        
            return redirect('success_page')
    else:
        form = DepositForm()
    return render(request, 'transactions/deposit.html', {'form': form})

@login_required
def transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST or None)
        if form.is_valid():
            recipientIBAN = form.cleaned_data['recipientIBAN']
            amount = form.cleaned_data['amount']
            sender_account = BankAccount.objects.get(user=request.user)
            recipient_account = BankAccount.objects.get(IBAN=recipientIBAN)
            type = form.cleaned_data['type']
            if sender_account.balance >= amount:
                sender_account.balance -= amount
                sender_account.save()
                recipient_account.balance += amount
                recipient_account.save()
                Transaction.objects.get_or_create(amount = amount,
                                                  account = sender_account,
                                                  content = f'Transfered {amount} from {sender_account} to {recipient_account}')

                transfer = Transfer(amount=amount, recipient_iban=recipientIBAN ,
                              transaction_id = Transaction.objects.latest())            
                transfer.save()
                return redirect('success_page')
            else:
                return render(request, 'transactions/error_page.html', {'error_message': 'Insufficient funds'})
    else:
        form = TransferForm()
    return render(request, 'transactions/transfer.html', {'form': form})

@login_required
def withdrawal(request):
    if request.method == 'POST':
        form = WithdrawalForm(request.POST or None)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            account = BankAccount.objects.get(owner=request.user)
            type = form.cleaned_data['type']
            if account.balance >= amount:
                account.balance -= amount
                account.save()
                Transaction.objects.get_or_create(amount = amount,
                                                account = account,
                                                content = f'Withdraw {amount} from {account}')
                
                withdrawal = Withdrawal(amount=amount,
                                   transaction_id = Transaction.objects.latest())
                withdrawal.save()

                return redirect('transactions/success_page')
            else:
                return render(request, 'transactions/error_page.html', {'error_message': 'Insufficient funds'})
    else:
        form = WithdrawalForm()
    return render(request, 'transactions/withdrawal.html', {'form': form})

@login_required 
def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST or None)    
        if form.is_valid():
            entity = form.cleaned_data['entity']
            reference = form.cleaned_data['reference']
            amount = form.cleaned_data['amount']
            type = form.cleaned_data['type']
            
            bank_account = BankAccount.objects.get(user=request.user)  

            if bank_account.balance >= amount:
                Transaction.objects.get_or_create(amount = amount,
                                                  account = bank_account,
                                                  content = f'Paid {amount} to entity {entity}')
                
                payment = Payment(entity=entity, reference=reference,
                                   amount=amount, 
                                   transaction_id = Transaction.objects.latest())
                payment.save()

                bank_account.balance -= amount
                bank_account.save()
                return redirect('transactions/success_page') 
            else:
                return render(request, 'transactions/error_page.html', {'error_message': 'Insufficient funds'}) 
        else:
            return render(request, 'transactions/error_page.html', {'error_message': 'Payment form not valid'})
    else:
        form = PaymentForm() 
    return render(request, 'transactions/bill_payment.html', {'form':form})

@login_required
def receipt(request, transaction_id):
    transaction = get_object_or_404(Transaction, transaction_id=transaction_id)
    return render(request, 'transactions/receipt.html', {'transaction': transaction})


@login_required
def balance_inquiry(request):
    holder = ATMUser.objects.get(django_user = request.user)
    account = BankAccount.objects.get(holders=holder)
    context = {'balance': account.balance}
    return render(request, 'transactions/balance_inquiry.html', context)

@login_required
def transaction_history(request):
    holder = ATMUser.objects.get(django_user = request.user)
    bank_account = BankAccount.objects.get(holders=holder)
    transactions = Transaction.objects.filter(account=bank_account)

    return render(request, 'transactions/transaction_history.html', {'transactions': transactions})


@login_required
def success_page(request):
    return render(request, 'transactions/success_page.html')

@login_required
def error_page(request):
    return render(request, 'transactions/error_page.html')