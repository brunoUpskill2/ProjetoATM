from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de utilizador (email ou número de telefone)')
    password = forms.CharField(label='Palavra-passe', widget=forms.PasswordInput)

class PinRecoveryForm(forms.Form):
    username = forms.CharField(label='Nome de utilizador (email ou número de telefone)')
    email = forms.EmailField(label='Endereço de email')
    phone_number = forms.CharField(label='Número de telefone')

class CreatePinForm(forms.Form):
    new_pin = forms.CharField(label='Novo PIN', widget=forms.PasswordInput)
    confirm_new_pin = forms.CharField(label='Confirmar Novo PIN', widget=forms.PasswordInput)

class ChangePinForm(forms.Form):
    current_pin = forms.CharField(label='PIN Atual', widget=forms.PasswordInput)
    new_pin = forms.CharField(label='Novo PIN', widget=forms.PasswordInput)
    confirm_new_pin = forms.CharField(label='Confirmar Novo PIN', widget=forms.PasswordInput)
