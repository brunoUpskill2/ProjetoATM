from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('user/create_pin/', views.create_pin_view, name='create_pin'),
    path('user/change_pin/', views.change_pin_view, name='change_pin'),
    path('logout',views.logout,name='user_logout'),
]