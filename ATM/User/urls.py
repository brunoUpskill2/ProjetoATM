from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('pin_recovery/', views.pin_recovery_view, name='pin_recovery'),
    path('pin_recovery_sms/', views.pin_recovery_sms_view, name='pin_recovery_sms'),  # Se você tiver uma visualização para recuperação de PIN via SMS
    path('change_pin/', views.change_pin_view, name='change_pin'),
    path('create_user/', views.create_user_view, name='create_user'),
    # Outras URLs podem ser adicionadas aqui conforme necessário
]
