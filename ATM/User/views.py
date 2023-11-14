from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
from .decorators import password_require, phone_number_require, anonymous_required
from .forms import (
    PhoneTokenForm,
    PhoneTokenConfirmForm,
    PasswordLoginForm,
    SetPasswordForm,
    ForgetPasswordForm,
)
from .limit_request import GenerateLimitation

<<<<<<< HEAD
# Create your views here.
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
=======
User = get_user_model()

def invalid_attempts_massage_view(request):
    """
    This function is executed when the number of user attempts to login
    or enter the code exceeds the allowed limit.
    """
    return render(request, "registration/invalid_attempts.html")


class GenerateToken(FormView):
    form_class = PhoneTokenForm
    template_name = "registration/generate_token.html"
    success_url = reverse_lazy("phone_login:confirm_otp")

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        GenerateLimitation(self.request)
        self.request.session["phone_number"] = form.phone_token.phone_number
        PhoneToken.send_otp(form.phone_token)
        return super().form_valid(form)

    @method_decorator(anonymous_required)
    @method_decorator(check_limitation)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ConfirmToken(FormView):
    form_class = PhoneTokenConfirmForm
    template_name = "registration/confirm_phone.html"
    success_url = "/"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request=request, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        login(
            self.request,
            form.user_cache,
            backend="django.contrib.auth.backends.ModelBackend",
        )
        del self.request.session["phone_number"]
        messages.success(self.request, "Successfully logged in.")
        return super().form_valid(form)

    @method_decorator(phone_number_require("login", "phone_number"))
    @method_decorator(check_limitation)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PasswordLogin(FormView):
    form_class = PasswordLoginForm
    template_name = "registration/password_login.html"
    success_url = "/"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request=request, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        login(
            self.request,
            form.user_cache,
            backend="django.contrib.auth.backends.ModelBackend",
        )
        del self.request.session["phone_number"]
        messages.success(self.request, "Successfully logged in.")
        return super().form_valid(form)

    @method_decorator(phone_number_require("login", "phone_number"))
    @method_decorator(check_limitation)
    @method_decorator(password_require)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ForgetPassword(FormView):
    form_class = ForgetPasswordForm
    template_name = "registration/forget_password.html"
    success_url = reverse_lazy("phone_login:confirm_password_otp")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request=request, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        GenerateLimitation(self.request)
        generate_token = PhoneToken.send_otp(form.phone_token)
        self.request.session[
            "phone_number_for_password"
        ] = form.phone_token.phone_number
        messages.success(self.request, "OTP sent successfully.")
        return super().form_valid(form)

    @method_decorator(check_limitation)
    @method_decorator(anonymous_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ConfirmPasswordToken(FormView):
    form_class = PhoneTokenConfirmForm
    template_name = "registration/confirm_phone.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request=request, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        phone_number = self.request.session.get("phone_number_for_password")
        user = get_object_or_404(User, phone=phone_number)
        uid = urlsafe_base64_encode(force_bytes(user))
        token = default_token_generator.make_token(user)
        del self.request.session["phone_number_for_password"]
        messages.success(self.request, "Phone number verified.")
        return redirect(
            reverse(
                "phone_login:change_password", kwargs={"uidb64": uid, "token": token}
            )
        )

    @method_decorator(
        phone_number_require("forget_password", "phone_number_for_password")
    )
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ChangePassword(FormView):
    form_class = SetPasswordForm
    template_name = "registration/change_password.html"
    success_url = "/"

    def get_user(self, uidb64):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User._default_manager.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user

    def get(self, request, *args, **kwargs):
        user = self.get_user(kwargs["uidb64"])
        if user is not None and default_token_generator.check_token(
            user, self.kwargs.get("token")
        ):
            return super().get(request, *args, **kwargs)
        messages.error(self.request, "Invalid link.")
        return HttpResponse("Invalid Link")

    def post(self, request, *args, **kwargs):
        user = self.get_user(kwargs["uidb64"])
        form = self.form_class(user=user, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        user = form.save()
        auth = authenticate(
            username=user.phone, password=form.cleaned_data["new_password2"]
        )
        if auth:
            login(
                self.request, user, backend="django.contrib.auth.backends.ModelBackend"
            )
        messages.success(self.request, "Password changed successfully.")
        return super().form_valid(form)
>>>>>>> 850a2bbd4906cad3c03d18f24aa64f38b1889aac
