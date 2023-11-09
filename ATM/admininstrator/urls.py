from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='admin-home'),
    path('admin-login', views.adminLogin, name='admin-login'),
    path('admin-logout', views.adminLogout, name='admin-logout'),
    path('atm-machine-status.html', views.atmMachineStatus, name='atm-machine-status'),
     
]