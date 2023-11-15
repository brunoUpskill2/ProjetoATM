from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm, CreatePinForm, ChangePinForm
from .models import ATMUser, PIN
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import the messages module


# Visualização de Login (Exemplo)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('base')
            else:
                form = LoginForm()  # Reset the form for re-rendering
                context = {'form': form, 'error_message': 'Authentication failed. Check your credentials.'}
                # Add an error message to the Django messages framework
                messages.error(request, 'Authentication failed. Check your credentials.')
                return render(request, 'user/login.html', context)
        else:
            form = LoginForm()
            context = {'form': form}
            return render(request, 'user/login.html', context)

# Visualização de Criação de PIN (Exemplo)
@login_required
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
    return render(request, 'user/create_pin.html', {'form': form})

# Visualização de Alteração de PIN (Exemplo)
@login_required
def change_pin_view(request):
    if request.method == 'POST':
        form = ChangePinForm(request.POST)
        if form.is_valid():
            user = request.user  # Obtém o usuário autenticado
            # Simule a alteração de um PIN de exemplo (você pode substituir por uma lógica real)
            new_pin = form.cleaned_data['new_pin']
            user.pin.pin = new_pin
            user.pin.save()
            return redirect('user/pin_changed')
    else:
        form = ChangePinForm()
    return render(request, 'user/change_pin.html', {'form': form})

@login_required
def user_logout(request):
    if request.method == 'GET':
        logout(request)
        redirect(request,'user/login.html')