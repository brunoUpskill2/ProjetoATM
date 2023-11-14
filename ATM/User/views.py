from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LoginForm, CreatePinForm, ChangePinForm
from .models import ATMUser, PIN

# Visualização de Login (Exemplo)
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return _extracted_from_login_view_(form, request)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# TODO Rename this here and in `login_view`
def _extracted_from_login_view_(form, request):
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']

    if username != 'exemplo@email.com' or password != 'senha':
        return render(request, 'login.html', {'form': form, 'error_message': 'Autenticação falhou. Verifique suas credenciais.'})
    user = ATMUser.objects.get(username='exemplo@email.com')
    login(request, user)
    return redirect('dashboard')

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





