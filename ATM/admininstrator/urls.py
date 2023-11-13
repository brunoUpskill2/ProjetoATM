from django.urls import path
from . import views

urlpatterns = [
    path('admins/admin-home', views.home, name='base'),
    path('admins/admin-login', views.adminLogin, name='admin-login'),
    path('admins/admin-logout', views.adminLogout, name='admin-logout'),
    path('admins/atm-machine-status.html', views.atmMachineStatus, name='atm-machine-status'),
    path('admins/view-transaction-history', views.view_transaction_history, name = 'view-transaction-history'), 
]