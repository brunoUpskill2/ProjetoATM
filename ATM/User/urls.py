from django.urls import path
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
