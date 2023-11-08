from django.db import models

# Create your models here.

class HolderType(models.Model):
    holderType_id = models.IntegerField(max_length=20)
    name = models.CharField(max_length=50)
    #1st Holder 
    #2nd Holder 
    #Mover 

class ATMUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    IBAN = models.CharField(max_length=25)
    BAN = models.CharField(max_length=21)
    NIF = models.CharField(max_length=9)    

class BankAccount(models.Model):
    account_id = models.AutoField(primary_key=True)
    holders = models.ManyToManyField(ATMUser,through='Holder')
    balance = models.DecimalField(max_digits=7,decimal_places=2)
    IBAN = models.CharField(max_length=25)

class Holder(models.Model):
    user = models.ForeignKey(ATMUser,on_delete=models.CASCADE)
    account = models.ForeignKey(BankAccount,on_delete=models.CASCADE)
    type = models.ForeignKey(HolderType,on_delete=models.CASCADE)

