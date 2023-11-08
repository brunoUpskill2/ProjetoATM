from django import forms

class FormularioLogin(forms.Form):
    username = forms.CharField(label='Nome de utilizador', max_length=255)
    password = forms.CharField(label='Palavra-passe', widget=forms.PasswordInput)

class FormularioRecuperacaoPinPorEmail(forms.Form):
    email = forms.EmailField(label='Endereço de email')

class FormularioMudarPin(forms.Form):
    pin_atual = forms.CharField(label='PIN Atual', widget=forms.PasswordInput)
    novo_pin = forms.CharField(label='Novo PIN', widget=forms.PasswordInput)
    confirmar_novo_pin = forms.CharField(label='Confirmar Novo PIN', widget=forms.PasswordInput)

class FormularioCriarUtilizador(forms.Form):
    username = forms.CharField(label='Nome de utilizador', max_length=255)
    password = forms.CharField(label='Palavra-passe', widget=forms.PasswordInput)
    confirmar_password = forms.CharField(label='Confirmar Palavra-passe', widget=forms.PasswordInput)
    email = forms.EmailField(label='Endereço de email')
    # Adicione outros campos necessários, como NIF, IBAN, etc.
