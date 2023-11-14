from django.urls import path
from .views import login_view, create_pin_view, change_pin_view

urlpatterns = [
    
    path('create_pin/', create_pin_view, name='create_pin'),
    path('change_pin/', change_pin_view, name='change_pin'),
    # Adicione outras URLs conforme necessário para seu projeto
]



from django.urls import path
from .views import (
    login_view,
    create_atm_user,
    
    create_bank_account,
    create_holder_type,
    create_holder,
    create_direct_holder,
    create_manual_holder,
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('create_atm_user/', create_atm_user, name='create_atm_user'),
    
    path('create_bank_account/', create_bank_account, name='create_bank_account'),
    path('create_holder_type/', create_holder_type, name='create_holder_type'),
    path('create_holder/', create_holder, name='create_holder'),
    path('create_direct_holder/', create_direct_holder, name='create_direct_holder'),
    path('create_manual_holder/', create_manual_holder, name='create_manual_holder'),
    # Adicione outras URLs conforme necessário
]
