from django.db import models
from user.models import ATMUser,BankAccount
from admininstrator.models import ATMMachine
# Create your models here.
class TransactionType(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = (
        ('canceled', 'Canceled'), 
        ('pending', 'Pending'), 
        ('complete', 'Complete')
    )

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7,decimal_places=2)
    
    type = models.ForeignKey(TransactionType,on_delete=models.CASCADE)
    recipientIBAN = models.CharField(max_length=25)
    

class Deposit(models.Model):
    deposit_id = models.AutoField(primary_key=True)
    transaction_id = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7,decimal_places=2)
    account = models.ForeignKey(BankAccount,on_delete=models.CASCADE)

class Withdrawal(models.Model):
    withdrawal_id = models.AutoField(primary_key=True)
    transaction_id = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7,decimal_places=2)
    
class Payment(models.Model): #######
    payment_id = models.AutoField(primary_key=True)
    transaction_id = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    entity = models.CharField(max_length=5)
    reference = models.CharField(max_length=9)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

class Receipt(models.Model):
    receipt_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=512)
    transaction_id = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(TransactionType,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(ATMUser,on_delete=models.CASCADE)
    atm_location = models.ForeignKey(ATMMachine,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.receipt_id},{self.content},{self.transaction_id},{self.timestamp},{self.user_id},{self.atm_location}"
    
