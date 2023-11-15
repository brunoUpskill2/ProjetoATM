from django.apps import AppConfig


class AdmininstratorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admininstrator'


from django.apps import AppConfig

class TransactionConfig(AppConfig):
    name = 'transactions'

class UserConfig(AppConfig):
    name = 'user'

