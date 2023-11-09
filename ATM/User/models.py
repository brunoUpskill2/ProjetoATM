from django.db import models

class HolderType(models.Model):
    holderType_id = models.IntegerField(max_length=20)
    name = models.CharField(max_length=50)

class ATMUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)  # Campo para senha

    def __str__(self):
        return self.username

class PIN(models.Model):
    user = models.ForeignKey(ATMUser, on_delete=models.CASCADE)
    pin = models.CharField(max_length=6)  # Campo para o PIN

class BankAccount(models.Model):
    account_id = models.AutoField(primary_key=True)
    holders = models.ManyToManyField(ATMUser, through='Holder')
    balance = models.FloatField(decimal_places=2)
    IBAN = models.CharField(max_length=25)

class Holder(models.Model):
    user = models.ForeignKey(ATMUser, on_delete=models.CASCADE)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    type = models.ForeignKey(HolderType, on_delete=models.CASCADE)
