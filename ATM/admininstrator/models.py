from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=20)
    managed_machines = models.ManyToManyField('ATMMachine')

class ATMMachine(models.Model):
    STATUS_CHOICES = (
    ("active", "Active"),
    ("deactivated", "Deactivated"))
    
    atm_machine_uid = models.CharField(
        primary_key=True,max_length=16,unique=True
        )
    
    current_balance = models.BigIntegerField()
    
    location = models.CharField(max_length=100)
    
    minimum_balance = models.BigIntegerField()

    status = models.CharField(
        max_length=15,
        choices = STATUS_CHOICES,
        default='active'
    )