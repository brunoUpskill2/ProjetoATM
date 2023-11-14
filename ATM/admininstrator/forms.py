from django import forms
from .models import ATMMachine

class AdminLoginForm(forms.Form):
    username = forms.CharField(label='username',max_length=20)
    password = forms.CharField(label='password',max_length=20,widget=forms.PasswordInput())

class TransactionSearchForm(forms.Form):
    recipient_iban = forms.CharField(label='Recipient IBAN',max_length=25)