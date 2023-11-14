"""
URL configuration for ATM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
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
    path('error_page', views.error_page, name='error_page'),
    path('receipt/<int:transaction_id>/', views.receipt, name='receipt')
]