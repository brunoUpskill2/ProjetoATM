from django.db import models
from user.models import ATMUser,BankAccount
from admininstrator.models import ATMMachine
# Create your models here.
class TransactionType(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2,default=0.00)
    transaction_types = models.ManyToManyField(TransactionType)
    recipientIBAN = models.CharField(max_length=25, null=True)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE,default=0)

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

class Receipt(models.Model):
    receipt_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=512)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE,default=4)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(ATMUser,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2,default=0.00)
    
    def __str__(self):
        return f"{self.receipt_id},{self.content},{self.transaction},{self.timestamp},{self.user},{self.amount}"
    
