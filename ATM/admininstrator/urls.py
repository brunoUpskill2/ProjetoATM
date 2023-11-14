from django.urls import path
from . import views

urlpatterns = [
    path('admins/home', views.home, name='base'),
    path('admins/atm-machine-status.html', views.atmMachineStatus, name='atm-machine-status'),
    path('admins/view-transaction-history', views.view_transaction_history, name = 'view-transaction-history'),
    path('admins/update_status/<str:atm_machine_uid>/', views.update_status, name='update_status'),

]