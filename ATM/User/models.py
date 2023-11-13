from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django_otp.models import TimeBasedOTP
from django_otp.oath import TOTP
from django_otp.util import hex_validator, random_hex

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('The Phone field must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone, password, **extra_fields)

class User(AbstractBaseUser, TimeBasedOTP):
    phone = models.CharField(max_length=20, unique=True, validators=[hex_validator], blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone

    def save(self, *args, **kwargs):
        # Ensure the phone number is in the correct format
        self.phone = self.phone.strip().lower()
        return super().save(*args, **kwargs)

    def get_totp_obj(self):
        key = random_hex().decode('utf-8')
        self.totp_key = key
        return TOTP(key)

    def verify_otp(self, otp):
        return self.totp_obj().verify(otp)

    def is_verified(self):
        return self.verified

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    @property
    def is_superuser(self):
        return self.is_staff

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
