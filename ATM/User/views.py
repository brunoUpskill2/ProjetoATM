from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login
from .forms import LoginForm, PinRecoveryForm, CreatePinForm, ChangePinForm
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


# Visualização de Recuperação de PIN por Email (Exemplo)
def pin_recovery_email(request):
    if request.method == 'POST':
        form = PinRecoveryForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = ATMUser.objects.filter(username=username, email=email).first()
            if user:
                # Gere um código de recuperação de exemplo (você pode substituir por uma lógica real)
                recovery_code = '123456'
                # Simule o envio do código de recuperação por email
                subject = 'Código de Recuperação de PIN'
                message = f'Seu código de recuperação é: {recovery_code}'
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
                return redirect('recovery_confirmation')
            else:
                return render(request, 'pin_recovery_email.html', {'form': form, 'error_message': 'Nenhuma correspondência encontrada.'})
    else:
        form = PinRecoveryForm()
    return render(request, 'pin_recovery_email.html', {'form': form})
# Visualização de Recuperação de PIN por SMS (Exemplo)
def pin_recovery_sms(request):
    if request.method == 'POST':
        form = PinRecoveryForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            phone_number = form.cleaned_data['phone_number']
            user = ATMUser.objects.filter(username=username, phone_number=phone_number).first()
            if user:
                # Gere um código de recuperação de exemplo (você pode substituir por uma lógica real)
                recovery_code = '123456'
                # Simule o envio do código de recuperação por SMS (substitua por lógica real)
                # Você pode usar serviços de SMS, como Twilio, para enviar o código.
                return redirect('recovery_confirmation')
            else:
                return render(request, 'pin_recovery_sms.html', {'form': form, 'error_message': 'Nenhuma correspondência encontrada.'})
    else:
        form = PinRecoveryForm()
    return render(request, 'pin_recovery_sms.html', {'form': form})

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