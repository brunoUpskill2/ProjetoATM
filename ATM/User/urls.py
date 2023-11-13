from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('pin_recovery_email/', views.pin_recovery_email, name='pin_recovery_email'),
    path('pin_recovery_sms/', views.pin_recovery_sms, name='pin_recovery_sms'),
    path('create_pin/', views.create_pin_view, name='create_pin'),
    path('change_pin/', views.change_pin_view, name='change_pin'),
]