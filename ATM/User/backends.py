# user/backends.py

from django.contrib.auth.backends import ModelBackend
from .models import ATMUser

class ATMUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = ATMUser.objects.get(username=username)
        except ATMUser.DoesNotExist:
            return None

        if user.django_user.check_password(password):
            return user

        return None
