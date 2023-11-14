from django.contrib import admin
from .models import ATMUser, PIN, BankAccount, HolderType, Holder

class ATMUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone')  # Adicione outros campos que deseja exibir na lista

admin.site.register(ATMUser, ATMUserAdmin)

class PINAdmin(admin.ModelAdmin):
    list_display = ('user', 'pin')  # Adicione outros campos que deseja exibir na lista

admin.site.register(PIN, PINAdmin)

class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'balance', 'IBAN')  # Adicione outros campos que deseja exibir na lista
    filter_horizontal = ('holders',)  # Torna a relação ManyToMany mais amigável no painel administrativo

admin.site.register(BankAccount, BankAccountAdmin)

class HolderTypeAdmin(admin.ModelAdmin):
    list_display = ('holderType_id', 'name')  # Adicione outros campos que deseja exibir na lista

admin.site.register(HolderType, HolderTypeAdmin)

class HolderAdmin(admin.ModelAdmin):
    list_display = ('user', 'account', 'type')  # Adicione outros campos que deseja exibir na lista

admin.site.register(Holder, HolderAdmin)


#################################################################
