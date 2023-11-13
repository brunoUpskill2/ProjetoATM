
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('deposit', views.deposit, name='deposit'),
    path('transfer', views.transfer, name='transfer'),
    path('withdrawal', views.withdrawal, name='withdrawal'),
    path('make_payment', views.make_payment, name='make_payment'),
    path('change_pin', views.change_pin, name='change_pin'),
    path('balance_inquiry', views.balance_inquiry, name='balance_inquiry'),
    path('transaction_history', views.transaction_history, name='transaction_history'),
    path('sucess_page', views.success_page, name='sucess_page'), 
    ]