# ATM/settings.py

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'sua_chave_secreta_aqui'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Transactions',
    'User',
    'otp',
    'otp.plugins.otp_static',
    'otp.plugins.otp_totp',
    'otp.plugins.otp_hotp',
    'otp.plugins.otp_sms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ATM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ATM.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações de envio de email (configure conforme apropriado)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'seu_servidor_de_email.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'cadudesporto@hotmail.com'  # Substitua pelo seu endereço de e-mail
EMAIL_HOST_PASSWORD = '1234'  # Substitua pela sua senha do Hotmail

# Configuração para envio de confirmação de email
DEFAULT_FROM_EMAIL = 'cadudesporto@hotmail.com'  # Substitua pelo seu endereço de e-mail
EMAIL_CONFIRMATION_DAYS = 1
EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
EMAIL_CONFIRMATION_COOLDOWN = 1800  # Meio dia em segundos
EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/login/'
EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/login/'

# Configuração de envio de SMS para o número fornecido
OTP_SMS_SENDER = '967131785'  # Substitua pelo número do qual você enviará o SMS
OTP_SMS_RECIPIENT_COUNTRY_CODE = '351'  # Substitua pelo código do seu país (Portugal)
OTP_SMS_RECIPIENT = '967131785'  # Substitua pelo seu número de telefone

# Configurações de Twilio (exemplo)
TWILIO_ACCOUNT_SID = 'seu_sid'
TWILIO_AUTH_TOKEN = 'seu_token'
TWILIO_PHONE_NUMBER = 'seu_numero_twilio'

# ... (outras configurações)

