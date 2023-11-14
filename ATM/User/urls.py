from django.urls import path
from .views import login_view, create_pin_view, change_pin_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('create_pin/', create_pin_view, name='create_pin'),
    path('change_pin/', change_pin_view, name='change_pin'),
    # Adicione outras URLs conforme necessário para seu projeto
]


