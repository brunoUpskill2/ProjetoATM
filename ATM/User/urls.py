from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('user/pin_recovery_email/', views.pin_recovery_email, name='pin_recovery_email'),
    path('user/pin_recovery_sms/', views.pin_recovery_sms, name='pin_recovery_sms'),
    path('user/create_pin/', views.create_pin_view, name='create_pin'),
    path('user/change_pin/', views.change_pin_view, name='change_pin'),
]
=======
from .views import (
    GenerateToken,
    ConfirmToken,
    PasswordLogin,
    ForgetPassword,
    ConfirmPasswordToken,
    ChangePassword,
    invalid_attempts_massage_view,
)

app_name = 'User'

urlpatterns = [
    path("login/", GenerateToken.as_view(), name="login"),
    path("confirm-otp/", ConfirmToken.as_view(), name="confirm_otp"),
    path("password-login/", PasswordLogin.as_view(), name="password_login"),
    path("forget-password/", ForgetPassword.as_view(), name="forget_password"),
    path("confirm-password-otp/", ConfirmPasswordToken.as_view(), name="confirm_password_otp"),
    path("change-password/<uidb64>/<token>/", ChangePassword.as_view(), name="change_password"),
    path("invalid-attempts/", invalid_attempts_massage_view, name="invalid_attempts_message"),
]
>>>>>>> 850a2bbd4906cad3c03d18f24aa64f38b1889aac
