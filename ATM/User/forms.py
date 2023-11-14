from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class CreatePinForm(forms.Form):
    new_pin = forms.CharField(label='New PIN', widget=forms.PasswordInput)

class ChangePinForm(forms.Form):
    new_pin = forms.CharField(label='New PIN', widget=forms.PasswordInput)




