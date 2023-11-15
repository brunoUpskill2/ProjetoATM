
from django.urls import path
from . import views
urlpatterns = [
    path('trans/home', views.home, name='home'),
    path('trans/balance_inquiry', views.balance_inquiry, name='balance_inquiry'),
    path('trans/bill_payment', views.make_payment, name='bill_payment'),
    path('trans/deposit', views.deposit, name='deposit'),
    path('trans/success_page', views.success_page, name='success_page'),
    path('trans/transaction_history', views.transaction_history, name='transaction_history'),
    path('trans/transfer', views.transfer, name='transfer'),
    path('trans/withdrawal', views.withdrawal, name='withdrawal'),
    path('trans/error_page', views.error_page, name='error_page'),
    path('trans/receipt/<int:transaction_id>/', views.receipt, name='receipt')
    ]