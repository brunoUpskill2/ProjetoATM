from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de Usuário Customizado
class ATMUser(AbstractUser):
    # Adicione campos personalizados conforme necessário
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

# Modelo para armazenar PINs dos usuários
class PIN(models.Model):
    user = models.OneToOneField(ATMUser, on_delete=models.CASCADE)
    pin = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.user.username} - PIN: {self.pin}'

# Modelo para informações da conta bancária
class BankAccount(models.Model):
    user = models.OneToOneField(ATMUser, on_delete=models.CASCADE)
    nib = models.CharField(max_length=15, blank=True, null=True)
    iban = models.CharField(max_length=34, blank=True, null=True)
    account_holder_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.account_holder_name} - NIB: {self.nib} - IBAN: {self.iban}'


###########################################################################################

from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de Usuário Customizado
class ATMUser(AbstractUser):
    # Adicione campos personalizados conforme necessário
    phone = models.CharField(max_length=15, blank=True, null=True)

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
