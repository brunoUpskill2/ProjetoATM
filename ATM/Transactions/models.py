from django.db import models
from User.models import ATMUser,BankAccount
from Admin.models import ATMMachine
# Create your models here.
class TransactionType(models.Model):
    type_id = models.IntegerField(max_length=25)
    name = models.CharField(max_length=50)
    status = (
        ('canceled', 'Canceled'), 
        ('pending', 'Pending'), 
        ('complete', 'Complete')
    )

class Transaction(models.Model):
    transaction_id = models.IntegerField(max_length=50,primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7,decimal_places=2)
    
    type = models.ForeignKey(TransactionType,on_delete=models.CASCADE)
    recipientIBAN = models.CharField(max_length=25)
    

class Deposit(models.Model):
    deposit_id = models.IntegerField(primary_key=True,max_length=250)
    transaction_id = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7,decimal_places=2)
    account = models.ForeignKey(BankAccount,on_delete=models.CASCADE)

class Withdrawal(models.Model):
    withdrawal_id = models.IntegerField(primary_key=True,max_length=250)
    transaction_id = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7,decimal_places=2)
    
    def processWithdrawal():
        pass
    def generateReceipt():
        pass

class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True,max_length=250)
    transaction_id = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7,decimal_places=2)
    recipientIBAN = models.CharField(max_length=25)
    description = models.CharField(max_length=255)

    def processPayment():
        pass
    def generateReceipt():
        pass

class Receipt(models.Model):
    receipt_id = models.IntegerField(primary_key=True,max_length=50)
    content = models.CharField(max_length=512)
    transaction_id = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(TransactionType,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(ATMUser,on_delete=models.CASCADE)
    atm_location = models.ForeignKey(ATMMachine,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.receipt_id},{self.content},{self.transaction_id},{self.timestamp},{self.user_id},{self.atm_location}"
    
