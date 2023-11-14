
from django.db import models
from django.contrib.auth.models import AbstractUser

from ATM import User

# Modelo de Usuário Customizado
class ATMUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    django_user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    # IBAN = models.CharField(max_length=25)
    # BAN = models.CharField(max_length=21)
    # NIF = models.CharField(max_length=9)    
   
    def __str__(self):
        return self.username

# Modelo para armazenar PINs dos usuários
class PIN(models.Model):
    user = models.ForeignKey(ATMUser, on_delete=models.CASCADE)
    pin = models.CharField(max_length=6)  # Campo para o PIN

# Modelo para informações da conta bancária
class BankAccount(models.Model):
    account_id = models.AutoField(primary_key=True)
    holders = models.ManyToManyField(ATMUser, through='Holder')
    balance = models.DecimalField(max_digits=7, decimal_places=2)
    IBAN = models.CharField(max_length=25)

class Holder(models.Model):
    user = models.ForeignKey(ATMUser, on_delete=models.CASCADE)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    type = models.ForeignKey('HolderType', on_delete=models.CASCADE)

class HolderType(models.Model):
    holderType_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    # 1st Holder
    # 2nd Holder
    # Mover
