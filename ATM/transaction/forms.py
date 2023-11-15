from django import forms

class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=15, decimal_places=2)

class TransferForm(forms.Form):
    recipientIBAN = forms.CharField(max_length=25)
    amount = forms.DecimalField(max_digits=15, decimal_places=2)

class WithdrawalForm(forms.Form):
    amount = forms.DecimalField(max_digits=15, decimal_places=2)

class PaymentForm(forms.Form):
    entity = forms.CharField(max_length=5)
    reference = forms.CharField(max_length=9)
    amount = forms.DecimalField(max_digits=15, decimal_places=2)
