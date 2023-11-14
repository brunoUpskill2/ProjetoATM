from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LoginForm, CreatePinForm, ChangePinForm
from .models import ATMUser, PIN

# Visualização de Login (Exemplo)
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Simulação de autenticação
            if username == 'exemplo@email.com' and password == 'senha':
                user = ATMUser.objects.get(username='exemplo@email.com')
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Autenticação falhou. Verifique suas credenciais.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Visualização de Criação de PIN (Exemplo)
def create_pin_view(request):
    if request.method == 'POST':
        form = CreatePinForm(request.POST)
        if form.is_valid():
            user = request.user  # Obtém o usuário autenticado

            # Simule a criação de um PIN de exemplo (você pode substituir por uma lógica real)
            new_pin = form.cleaned_data['new_pin']
            PIN.objects.create(user=user, pin=new_pin)

            return redirect('pin_created')
    else:
        form = CreatePinForm()
    return render(request, 'create_pin.html', {'form': form})

# Visualização de Alteração de PIN (Exemplo)
def change_pin_view(request):
    if request.method == 'POST':
        form = ChangePinForm(request.POST)
        if form.is_valid():
            user = request.user  # Obtém o usuário autenticado

            # Simule a alteração de um PIN de exemplo (você pode substituir por uma lógica real)
            new_pin = form.cleaned_data['new_pin']
            user.pin.pin = new_pin
            user.pin.save()

            return redirect('pin_changed')
    else:
        form = ChangePinForm()
    return render(request, 'change_pin.html', {'form': form})






######################################################################################


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ATMUserForm, PINForm, BankAccountForm, HolderTypeForm, HolderForm, DirectHolderForm, ManualHolderForm
from .models import ATMUser, PIN, BankAccount, HolderType, Holder

def create_atm_user(request):
    if request.method == 'POST':
        form = ATMUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Substitua 'success_page' pela página desejada
    else:
        form = ATMUserForm()
    return render(request, 'create_atm_user.html', {'form': form})


def create_bank_account(request):
    if request.method == 'POST':
        form = BankAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Substitua 'success_page' pela página desejada
    else:
        form = BankAccountForm()
    return render(request, 'create_bank_account.html', {'form': form})

def create_holder_type(request):
    if request.method == 'POST':
        form = HolderTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Substitua 'success_page' pela página desejada
    else:
        form = HolderTypeForm()
    return render(request, 'create_holder_type.html', {'form': form})

def create_holder(request):
    if request.method == 'POST':
        form = HolderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Substitua 'success_page' pela página desejada
    else:
        form = HolderForm()
    return render(request, 'create_holder.html', {'form': form})

def create_direct_holder(request):
    if request.method == 'POST':
        form = DirectHolderForm(request.POST)
        if form.is_valid():
            # Adiciona manualmente o 'type' antes de salvar
            form.cleaned_data['type'] = HolderType.objects.get(name='SeuTipoAqui')  # Substitua 'SeuTipoAqui' pelo nome desejado
            form.save()
            return redirect('success_page')  # Substitua 'success_page' pela página desejada
    else:
        form = DirectHolderForm()
    return render(request, 'create_direct_holder.html', {'form': form})

def create_manual_holder(request):
    if request.method == 'POST':
        form = ManualHolderForm(request.POST)
        if form.is_valid():
            # Adiciona manualmente o 'type' antes de salvar
            form.cleaned_data['type'] = HolderType.objects.get(name='SeuTipoAqui')  # Substitua 'SeuTipoAqui' pelo nome desejado
            Holder.objects.create(
                user=form.cleaned_data['user'],
                account=form.cleaned_data['account'],
                type=form.cleaned_data['type']
            )
            return redirect('success_page')  # Substitua 'success_page' pela página desejada
    else:
        form = ManualHolderForm()
    return render(request, 'create_manual_holder.html', {'form': form})
