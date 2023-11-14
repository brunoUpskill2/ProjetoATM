from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class PinRecoveryForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email')

class CreatePinForm(forms.Form):
    new_pin = forms.CharField(label='New PIN', widget=forms.PasswordInput)

class ChangePinForm(forms.Form):
    new_pin = forms.CharField(label='New PIN', widget=forms.PasswordInput)



###########################################

from django import forms
from .models import ATMUser, BankAccount, PIN, HolderType, Holder

class ATMUserForm(forms.ModelForm):
    class Meta:
        model = ATMUser
        fields = ['username', 'password', 'phone']

class PINForm(forms.ModelForm):
    class Meta:
        model = PIN
        fields = ['user', 'pin']

class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ['holders', 'balance', 'IBAN']

class HolderTypeForm(forms.ModelForm):
    class Meta:
        model = HolderType
        fields = ['name']

class HolderForm(forms.ModelForm):
    class Meta:
        model = Holder
        fields = ['user', 'account', 'type']

# Adicione um formulário adicional para criar um Holder diretamente
class DirectHolderForm(forms.ModelForm):
    class Meta:
        model = Holder
        fields = ['user', 'account']  # Excluído 'type' para ser adicionado manualmente

# Se você quiser adicionar manualmente o 'type', você pode fazer assim:
class ManualHolderForm(forms.Form):
    user = forms.ModelChoiceField(queryset=ATMUser.objects.all())
    account = forms.ModelChoiceField(queryset=BankAccount.objects.all())
    type = forms.ModelChoiceField(queryset=HolderType.objects.all())
