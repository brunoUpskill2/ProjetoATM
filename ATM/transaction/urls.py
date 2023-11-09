
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('balance_inquiry', views.balance_inquiry, name='balance_inquiry'),
    path('bill_payment', views.bill_payment, name='bill_payment'),
    path('change_pin', views.change_pin, name='change_pin'),
    path('deposit', views.deposit, name='deposit'),
    path('success_page', views.success_page, name='success_page'),
    path('transaction_history', views.transaction_history, name='transaction_history'),
    path('transfer', views.transfer, name='transfer'),
    path('withdrawal', views.withdrawal, name='withdrawal'), 
    ]