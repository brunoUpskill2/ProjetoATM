
from django.urls import path
from . import views
urlpatterns = [
    path('admin-home', views.home, name='home'),
    path('<int:/deposit', views.deposit, name='deposit'),
    path('action/transfer', views.transfer, name='transfer'),
    path('action/withdrawal', views.withdrawal, name='withdrawal'),
    path('action/make_payment', views.make_payment, name='make_payment'),
    path('action/change_pin', views.change_pin, name='change_pin'),
    path('action/balance_inquiry', views.balance_inquiry, name='balance_inquiry'),
    path('action/transaction_history', views.transaction_history, name='transaction_history'),
    path('action/sucess_page', views.success_page, name='sucess_page'), 
    ]