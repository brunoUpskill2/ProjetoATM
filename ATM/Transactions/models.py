from django.db import models
from .models import  BankAccount

class TransactionType(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2,default=0.00)
    transaction_type = models.ForeignKey(TransactionType)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE,default=0)
    content = models.CharField(max_length=500)
    
          
class Deposit(models.Model):
    deposit_id = models.AutoField(primary_key=True)
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE,default=1)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE,default=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2,default=0.00)
    
class Withdrawal(models.Model):
    withdrawal_id = models.AutoField(primary_key=True)
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE,default=2)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE,default=3)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2,default=0.00)
    
class Payment(models.Model): #######
    payment_id = models.AutoField(primary_key=True)
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE,default=3)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE,default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    entity = models.CharField(max_length=5)
    reference = models.CharField(max_length=9)
    amount = models.DecimalField(max_digits=15, decimal_places=2,default=0.00)


class Transfer(models.Model):
    transfer_id = models.IntegerField(primary_key=True)
    transaction_id = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=25,decimal_places=2,default=0.00)
    recipient_iban = models.CharField(max_length=23)

    
