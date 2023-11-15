from django import forms
<<<<<<< HEAD

=======
>>>>>>> e94945758e1e6b236ce8cc8395cd3680e858ea9a
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

<<<<<<< HEAD
=======
class PinRecoveryForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email')

>>>>>>> e94945758e1e6b236ce8cc8395cd3680e858ea9a
class CreatePinForm(forms.Form):
    new_pin = forms.CharField(label='New PIN', widget=forms.PasswordInput)

class ChangePinForm(forms.Form):
    new_pin = forms.CharField(label='New PIN', widget=forms.PasswordInput)
<<<<<<< HEAD




=======
>>>>>>> e94945758e1e6b236ce8cc8395cd3680e858ea9a
