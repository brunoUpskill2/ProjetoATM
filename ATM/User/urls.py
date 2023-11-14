from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('user/pin_recovery_email/', views.pin_recovery_email, name='pin_recovery_email'),
    path('user/pin_recovery_sms/', views.pin_recovery_sms, name='pin_recovery_sms'),
    path('user/create_pin/', views.create_pin_view, name='create_pin'),
    path('user/change_pin/', views.change_pin_view, name='change_pin'),
]