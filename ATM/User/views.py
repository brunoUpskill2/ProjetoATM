from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, PinRecoveryForm, ChangePinForm, CreateUserForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirecione para a página de sucesso ou a página desejada após o login.
                return redirect('sucesso')
            else:
                # Trate a autenticação falhada aqui, por exemplo, exiba uma mensagem de erro.
                return render(request, 'login.html', {'form': form, 'error_message': 'Autenticação falhou. Verifique suas credenciais.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




def pin_recovery_view(request):
    if request.method == 'POST':
        form = PinRecoveryForm(request.POST)
        if form.is_valid():
            # Lógica para enviar um e-mail de recuperação de PIN.
            # Vou adicionar uma lógica simples aqui para enviar um e-mail com o PIN.
            
            # Suponha que você tenha um atributo 'email' no seu formulário.
            user_email = form.cleaned_data['email']
            # Gere um PIN aleatório (você pode usar outras bibliotecas para isso).
            import random
            pin = ''.join(random.choice('0123456789') for i in range(6))

            # Agora você pode enviar um e-mail com o PIN.
            # Certifique-se de configurar suas configurações de e-mail no settings.py.
            from django.core.mail import send_mail
            subject = 'Recuperação de PIN'
            message = f'Seu novo PIN é: {pin}'
            from_email = 'seu_email@gmail.com'  # Substitua pelo seu e-mail
            recipient_list = [user_email]
            send_mail(subject, message, from_email, recipient_list)

            return redirect('email_enviado')  # Redirecionar após o e-mail ser enviado
    else:
        form = PinRecoveryForm()
    return render(request, 'pin_recovery.html', {'form': form})


def change_pin_view(request):
    if request.method == 'POST':
        form = ChangePinForm(request.POST)
        if form.is_valid():
            # Lógica para verificar e mudar o PIN do usuário.
            # Implemente a lógica de mudança de PIN aqui.
            return redirect('pin_mudado')
    else:
        form = ChangePinForm()
    return render(request, 'change_pin.html', {'form': form})

def create_user_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Lógica para criar um novo usuário.
            # Implemente a lógica de criação de usuário aqui.
            return redirect('novo_usuario_criado')
    else:
        form = CreateUserForm()
    return render(request, 'create_user.html', {'form': form})
