from django.urls import path
from .views import login_view, create_pin, change_pin



from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('user/create_pin/', views.create_pin_view, name='create_pin'),
    path('user/change_pin/', views.change_pin_view, name='change_pin'),
]

