from django.contrib import admin
from .models import PhoneToken

# Register your models here.

@admin.register(PhoneToken)
class PhoneTokenAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'otp', 'timestamp', 'ip_address']
    search_fields = ['phone_number']
    list_filter = ['timestamp']
