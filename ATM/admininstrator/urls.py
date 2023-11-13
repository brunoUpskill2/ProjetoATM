from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='base'),
    path('admin-login', views.adminLogin, name='admin-login'),
    path('admin-logout', views.adminLogout, name='admin-logout'),
    path('atm-machine-status.html', views.atmMachineStatus, name='atm-machine-status'),
    path('view-transaction-history', views.view_transaction_history, name = 'view-transaction-history'), 
]