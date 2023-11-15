from django.urls import path
from .views import login_view, create_pin, change_pin



from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
<<<<<<< HEAD
=======
    path('user/pin_recovery_email/', views.pin_recovery_email, name='pin_recovery_email'),
    path('user/pin_recovery_sms/', views.pin_recovery_sms, name='pin_recovery_sms'),
>>>>>>> e94945758e1e6b236ce8cc8395cd3680e858ea9a
    path('user/create_pin/', views.create_pin_view, name='create_pin'),
    path('user/change_pin/', views.change_pin_view, name='change_pin'),
]

