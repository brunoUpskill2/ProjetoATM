from django.contrib import admin
from Transactions.models import *
from User.models import *
from Admin.models import *

# Register your models here.
#Admin
admin.site.register(Admin)
admin.site.register(ATMMachine)
#Transactions
admin.site.register(TransactionType)
admin.site.register(Transaction)
admin.site.register(Deposit)
admin.site.register(Withdrawal)
admin.site.register(Payment)
admin.site.register(Receipt)
#User
admin.site.register(HolderType)
admin.site.register(Holder)
admin.site.register(ATMUser)
admin.site.register(BankAccount)